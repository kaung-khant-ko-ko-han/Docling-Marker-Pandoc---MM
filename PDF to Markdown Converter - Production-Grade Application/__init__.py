"""
PDF to Markdown Converter - Production-Grade Application

A comprehensive Python application for converting PDF documents to Markdown format
using the Marker library, with features for chapter splitting, translation chunking,
image extraction, and quality validation.
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .config import load_config
from .converter import PDFConverter, batch_convert
from .models import ConversionConfig, AppConfig, Metadata
from .validator import MarkdownValidator
from .chapter_splitter import ChapterSplitter
from .chunker import MarkdownChunker
from .utils import setup_logging, ensure_dir

__all__ = [
    "load_config",
    "PDFConverter",
    "batch_convert",
    "ConversionConfig",
    "AppConfig",
    "Metadata",
    "MarkdownValidator",
    "ChapterSplitter",
    "MarkdownChunker",
    "setup_logging",
    "ensure_dir",
]
