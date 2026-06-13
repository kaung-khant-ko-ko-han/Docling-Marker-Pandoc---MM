"""Extract metadata from PDF files."""

from pathlib import Path
from typing import Dict, Any
import logging
import PyPDF2

logger = logging.getLogger(__name__)


def extract_pdf_metadata(pdf_path: Path) -> Dict[str, Any]:
    """Extract title, author, language, page count from PDF."""
    metadata = {
        "title": None,
        "author": None,
        "pages": 0,
        "language": None,
    }
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            info = reader.metadata
            if info:
                metadata["title"] = info.get("/Title", "").strip()
                metadata["author"] = info.get("/Author", "").strip()
                # Language is not standard; try /Lang
                metadata["language"] = info.get("/Lang", None)
            metadata["pages"] = len(reader.pages)
    except Exception as e:
        logger.warning(f"Failed to extract PDF metadata from {pdf_path}: {e}")
    
    return metadata
