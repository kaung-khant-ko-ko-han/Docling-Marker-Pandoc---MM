"""Core conversion logic using Marker PDF library."""

import time
import shutil
from pathlib import Path
from typing import Optional, Tuple, List
import logging
from tqdm import tqdm

from marker.convert import convert_single_pdf
from marker.models import load_all_models
from marker.config.parser import ConfigParser

from .models import ConversionConfig, Metadata, Checkpoint
from .utils import ensure_dir, save_checkpoint, load_checkpoint, count_markdown_tables
from .metadata import extract_pdf_metadata

logger = logging.getLogger(__name__)


class PDFConverter:
    """Handles PDF to Markdown conversion with resume and progress tracking."""
    
    def __init__(self, config: ConversionConfig):
        self.config = config
        self.models = None  # Lazy load marker models
        self.checkpoint = None
        if config.resume:
            self.checkpoint = load_checkpoint(config.input_path, config.output_dir)
    
    def _load_marker_models(self):
        """Load marker models once."""
        if self.models is None:
            logger.info("Loading Marker models (this may take a while on first run)...")
            self.models = load_all_models()
    
    def convert(self) -> Tuple[Path, Metadata]:
        """Convert PDF to Markdown. Returns (markdown_path, metadata)."""
        start_time = time.time()
        input_path = self.config.input_path
        output_dir = self.config.output_dir
        ensure_dir(output_dir)
        
        # Determine page range
        page_range = None
        if self.config.page_start or self.config.page_end:
            page_range = (self.config.page_start or 0, self.config.page_end or 999999)
        
        # Resume support: if checkpoint exists, resume from last page
        if self.checkpoint and self.checkpoint.last_processed_page > 0:
            logger.info(f"Resuming from page {self.checkpoint.last_processed_page + 1}")
            page_range = (self.checkpoint.last_processed_page, page_range[1] if page_range else 999999)
        
        # Convert using marker
        self._load_marker_models()
        config_parser = ConfigParser()
        
        # Configure output
        output_path = output_dir / f"{input_path.stem}.md"
        images_dir = output_dir / "images"
        ensure_dir(images_dir)
        
        logger.info(f"Converting {input_path.name}...")
        try:
            full_text, images, out_meta = convert_single_pdf(
                input_path,
                self.models,
                config_parser.generate_config_dict(),
                page_range=page_range,
            )
        except Exception as e:
            logger.error(f"Marker conversion failed: {e}")
            raise
        
        # Write markdown
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_text)
        
        # Save images
        image_count = 0
        if self.config.extract_images and images:
            for img_name, img_data in images.items():
                img_path = images_dir / img_name
                with open(img_path, "wb") as img_file:
                    img_file.write(img_data)
                image_count += 1
            # Update markdown links to relative paths
            self._fix_image_links(output_path, images_dir)
        
        # Extract metadata from PDF
        pdf_meta = extract_pdf_metadata(input_path)
        
        # Count tables
        table_count = count_markdown_tables(full_text)
        
        metadata = Metadata(
            title=pdf_meta.get("title") or input_path.stem,
            author=pdf_meta.get("author"),
            pages=out_meta.get("total_pages", 0),
            language=pdf_meta.get("language"),
            images=image_count,
            tables=table_count,
            conversion_time_seconds=time.time() - start_time,
            output_path=output_path,
        )
        
        # Save checkpoint after completion
        if self.config.resume:
            final_checkpoint = Checkpoint(
                input_path=self.config.input_path,
                output_dir=self.config.output_dir,
                last_processed_page=metadata.pages,
                total_pages=metadata.pages,
            )
            save_checkpoint(final_checkpoint, output_dir / ".checkpoints")
        
        logger.info(f"Conversion complete: {output_path}")
        return output_path, metadata
    
    def _fix_image_links(self, md_path: Path, images_dir: Path):
        """Update image links to point to local images directory."""
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        import re
        # Replace marker's absolute paths with relative images/
        pattern = r'!\[(.*?)\]\((.*?)\)'
        def repl(match):
            alt = match.group(1)
            path = match.group(2)
            # If path is a filename, assume it's in images_dir
            filename = Path(path).name
            new_path = f"images/{filename}"
            return f"![{alt}]({new_path})"
        
        new_content = re.sub(pattern, repl, content)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(new_content)


def batch_convert(input_dir: Path, output_dir: Path, workers: int, config_overrides: dict):
    """Convert multiple PDFs in parallel using multiprocessing."""
    from concurrent.futures import ProcessPoolExecutor, as_completed
    from .config import AppConfig
    import sys
    
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    ensure_dir(output_dir)
    
    pdf_files = list(input_dir.glob("*.pdf"))
    logger.info(f"Found {len(pdf_files)} PDF files to convert")
    
    # Prepare per-file output dirs
    jobs = []
    for pdf in pdf_files:
        out_subdir = output_dir / pdf.stem
        ensure_dir(out_subdir)
        cfg = ConversionConfig(
            input_path=pdf,
            output_dir=out_subdir,
            extract_images=config_overrides.get("extract_images", True),
            split_chapters=config_overrides.get("split_chapters", False),  # handled separately
            chunk_for_translation=False,
            resume=False,
            workers=1,
        )
        jobs.append(cfg)
    
    # Process sequentially if workers=1 else parallel
    if workers <= 1:
        results = []
        for job in tqdm(jobs, desc="Converting PDFs"):
            converter = PDFConverter(job)
            try:
                md_path, meta = converter.convert()
                results.append((job.input_path, meta))
            except Exception as e:
                logger.error(f"Failed to convert {job.input_path}: {e}")
                results.append((job.input_path, None))
        return results
    else:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(_convert_job, job): job for job in jobs}
            results = []
            for future in tqdm(as_completed(futures), total=len(jobs), desc="Converting PDFs"):
                job = futures[future]
                try:
                    md_path, meta = future.result()
                    results.append((job.input_path, meta))
                except Exception as e:
                    logger.error(f"Failed to convert {job.input_path}: {e}")
                    results.append((job.input_path, None))
        return results


def _convert_job(job_config: ConversionConfig):
    """Helper for multiprocessing."""
    # Re-import inside function to avoid pickling issues
    from .converter import PDFConverter
    converter = PDFConverter(job_config)
    return converter.convert()
