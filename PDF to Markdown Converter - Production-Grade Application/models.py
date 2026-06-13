"""Pydantic models for configuration, metadata, and validation."""

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List, Dict, Any
from pathlib import Path
from datetime import datetime


class ConversionConfig(BaseModel):
    """Configuration for a conversion job."""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    input_path: Path
    output_dir: Path
    extract_images: bool = True
    split_chapters: bool = True
    chunk_for_translation: bool = True
    resume: bool = False
    page_start: Optional[int] = None
    page_end: Optional[int] = None
    workers: int = 1


class AppConfig(BaseModel):
    """Overall application configuration from YAML."""
    input_dir: Path = Path("./books")
    output_dir: Path = Path("./output")
    chunk_size: int = 20000  # characters
    chunk_lines: int = 1000   # fallback
    workers: int = 4
    extract_images: bool = True
    split_chapters: bool = True
    validation_enabled: bool = True
    checkpoint_interval: int = 10  # pages
    chapter_patterns: List[str] = [
        r"^#\s+(?:Chapter|Part|Section)\s+\d+",
        r"^##\s+\d+\.\d+",
        r"^#{1,6}\s+.+",  # any heading
    ]
    image_formats: List[str] = [".png", ".jpg", ".jpeg"]
    log_level: str = "INFO"
    
    model_config = ConfigDict(extra="ignore")


class Metadata(BaseModel):
    """Metadata extracted from PDF and conversion run."""
    title: Optional[str] = None
    author: Optional[str] = None
    pages: int = 0
    language: Optional[str] = None
    chapters: int = 0
    images: int = 0
    tables: int = 0
    conversion_time_seconds: float = 0.0
    output_path: Path
    checkpoint_path: Optional[Path] = None
    created_at: datetime = Field(default_factory=datetime.now)


class ValidationIssue(BaseModel):
    """Single validation issue."""
    type: str  # "broken_image", "unclosed_code_block", etc.
    file: str
    line: Optional[int] = None
    description: str
    severity: str  # "error", "warning"


class ValidationReport(BaseModel):
    """Full validation report."""
    issues: List[ValidationIssue] = []
    total_errors: int = 0
    total_warnings: int = 0
    markdown_file: str
    validated_at: datetime = Field(default_factory=datetime.now)


class Checkpoint(BaseModel):
    """Resume checkpoint data."""
    input_path: Path
    output_dir: Path
    last_processed_page: int
    total_pages: int
    completed_chunks: List[str] = []
    timestamp: datetime = Field(default_factory=datetime.now)
