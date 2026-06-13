"""CLI entry point using Typer."""

import typer
from pathlib import Path
from typing import Optional
import json
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

from .config import load_config
from .converter import PDFConverter, batch_convert
from .models import ConversionConfig, AppConfig
from .chapter_splitter import ChapterSplitter
from .chunker import MarkdownChunker
from .validator import MarkdownValidator
from .utils import setup_logging, ensure_dir
from .metadata import extract_pdf_metadata

app = typer.Typer(help="Production PDF to Markdown converter using Marker")
console = Console()


@app.command()
def convert(
    pdf_path: Path = typer.Argument(..., help="Path to PDF file"),
    output_dir: Path = typer.Option(None, help="Output directory (default: config output_dir/pdfname)"),
    resume: bool = typer.Option(False, help="Resume from last checkpoint"),
    page_start: Optional[int] = typer.Option(None, help="Start page (1-indexed)"),
    page_end: Optional[int] = typer.Option(None, help="End page"),
    workers: int = typer.Option(1, help="Number of workers (parallel pages not supported in single, use batch)"),
    no_images: bool = typer.Option(False, help="Do not extract images"),
    no_split: bool = typer.Option(False, help="Do not split chapters"),
    no_chunk: bool = typer.Option(False, help="Do not create translation chunks"),
):
    """Convert a single PDF to Markdown."""
    config = load_config()
    setup_logging(config.log_level)
    
    if output_dir is None:
        output_dir = config.output_dir / pdf_path.stem
    ensure_dir(output_dir)
    
    # Override from CLI
    extract_images = not no_images
    split_chapters = not no_split
    chunk_for_translation = not no_chunk
    
    conv_config = ConversionConfig(
        input_path=pdf_path,
        output_dir=output_dir,
        extract_images=extract_images,
        split_chapters=False,  # handled after conversion
        chunk_for_translation=False,
        resume=resume,
        page_start=page_start,
        page_end=page_end,
        workers=workers,
    )
    
    converter = PDFConverter(conv_config)
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Converting...", total=None)
        md_path, metadata = converter.convert()
    
    console.print(f"[green]✓ Conversion complete[/green]")
    console.print(f"Markdown: {md_path}")
    console.print(f"Images: {metadata.images} extracted")
    console.print(f"Tables: {metadata.tables}")
    
    # Save metadata
    meta_path = output_dir / "metadata.json"
    with open(meta_path, "w") as f:
        json.dump(metadata.model_dump(), f, indent=2, default=str)
    
    # Chapter splitting
    if split_chapters:
        splitter = ChapterSplitter(config)
        chapters_dir = output_dir / "chapters"
        splitter.split(md_path, chapters_dir)
        metadata.chapters = len(list(chapters_dir.glob("*.md")))
        console.print(f"[green]✓ Split into {metadata.chapters} chapters[/green]")
    
    # Chunk for translation
    if chunk_for_translation:
        chunker = MarkdownChunker(config)
        chunks_dir = output_dir / "chunks"
        chunker.chunk_file(md_path, chunks_dir)
        console.print(f"[green]✓ Created translation chunks in {chunks_dir}[/green]")
    
    # Validation
    if config.validation_enabled:
        validator = MarkdownValidator()
        report = validator.validate_file(md_path, output_dir / "images")
        if report.total_errors > 0:
            console.print(f"[red]Validation found {report.total_errors} errors[/red]")
            for issue in report.issues:
                if issue.severity == "error":
                    console.print(f"  - {issue.description}")
        else:
            console.print("[green]✓ Validation passed[/green]")
        # Save report
        report_path = output_dir / "validation_report.json"
        with open(report_path, "w") as f:
            json.dump(report.model_dump(), f, indent=2, default=str)


@app.command()
def batch(
    input_dir: Path = typer.Argument(..., help="Directory containing PDF files"),
    output_dir: Path = typer.Option(None, help="Output root directory"),
    workers: int = typer.Option(4, help="Number of parallel workers"),
    no_images: bool = typer.Option(False, help="Do not extract images"),
):
    """Batch convert multiple PDFs."""
    config = load_config()
    setup_logging(config.log_level)
    
    if output_dir is None:
        output_dir = config.output_dir
    
    ensure_dir(output_dir)
    
    overrides = {
        "extract_images": not no_images,
        "split_chapters": True,
        "chunk_for_translation": True,
    }
    
    results = batch_convert(input_dir, output_dir, workers, overrides)
    
    # Summary table
    table = Table(title="Batch Conversion Summary")
    table.add_column("PDF", style="cyan")
    table.add_column("Pages", style="magenta")
    table.add_column("Images", style="green")
    table.add_column("Tables", style="yellow")
    table.add_column("Status", style="white")
    
    for pdf_path, meta in results:
        if meta:
            table.add_row(pdf_path.name, str(meta.pages), str(meta.images), str(meta.tables), "✓")
        else:
            table.add_row(pdf_path.name, "-", "-", "-", "✗ Failed")
    
    console.print(table)


@app.command()
def validate(
    markdown_file: Path = typer.Argument(..., help="Markdown file to validate"),
    images_dir: Optional[Path] = typer.Option(None, help="Images directory for link checking"),
):
    """Validate a generated markdown file."""
    config = load_config()
    setup_logging(config.log_level)
    
    validator = MarkdownValidator()
    report = validator.validate_file(markdown_file, images_dir)
    
    console.print(f"Validation of {markdown_file}")
    console.print(f"Errors: {report.total_errors}, Warnings: {report.total_warnings}")
    for issue in report.issues:
        color = "red" if issue.severity == "error" else "yellow"
        console.print(f"[{color}]• {issue.description}[/{color}]")
    
    # Save report
    report_path = markdown_file.parent / "validation_report.json"
    with open(report_path, "w") as f:
        json.dump(report.model_dump(), f, indent=2, default=str)
    console.print(f"Report saved to {report_path}")


if __name__ == "__main__":
    app()
