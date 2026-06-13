"""Helper functions: logging, file operations, checkpoint handling."""

import logging
import json
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, Optional
from rich.logging import RichHandler
from .models import Checkpoint


def setup_logging(level: str = "INFO") -> None:
    """Configure rich logging."""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )


def save_checkpoint(checkpoint: Checkpoint, checkpoint_dir: Path) -> None:
    """Save checkpoint to disk."""
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_file = checkpoint_dir / f"{checkpoint.input_path.stem}_checkpoint.json"
    with open(checkpoint_file, "w", encoding="utf-8") as f:
        json.dump(checkpoint.model_dump(), f, indent=2, default=str)


def load_checkpoint(input_path: Path, output_dir: Path) -> Optional[Checkpoint]:
    """Load checkpoint if exists."""
    checkpoint_dir = output_dir / ".checkpoints"
    checkpoint_file = checkpoint_dir / f"{input_path.stem}_checkpoint.json"
    if checkpoint_file.exists():
        with open(checkpoint_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return Checkpoint(**data)
    return None


def ensure_dir(path: Path) -> None:
    """Create directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)


def count_markdown_tables(markdown_text: str) -> int:
    """Count simple markdown tables (rows with |)."""
    lines = markdown_text.splitlines()
    count = 0
    in_table = False
    for line in lines:
        if line.startswith("|") and "|" in line:
            if not in_table:
                count += 1
                in_table = True
        elif in_table and not line.strip():
            in_table = False
    return count


def extract_image_links(markdown_text: str) -> list:
    """Extract all markdown image links ![alt](path)."""
    import re
    pattern = r'!\[.*?\]\((.*?)\)'
    return re.findall(pattern, markdown_text)
