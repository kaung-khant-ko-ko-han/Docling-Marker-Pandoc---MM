"""Detect chapters in markdown and split into separate files."""

import re
from pathlib import Path
from typing import List, Tuple, Optional
import logging

from .models import AppConfig

logger = logging.getLogger(__name__)


class ChapterSplitter:
    """Split markdown into chapter files based on heading patterns."""
    
    def __init__(self, config: AppConfig):
        self.patterns = [re.compile(p, re.IGNORECASE) for p in config.chapter_patterns]
    
    def detect_chapters(self, markdown_text: str) -> List[Tuple[int, str, int]]:
        """
        Detect chapter boundaries.
        Returns list of (start_line_index, heading_text, heading_level).
        """
        lines = markdown_text.splitlines()
        chapters = []
        
        for i, line in enumerate(lines):
            for pattern in self.patterns:
                match = pattern.match(line.strip())
                if match:
                    # Determine heading level by counting # at start (FIXED)
                    level = self._count_heading_level(line.strip())
                    chapters.append((i, line.strip(), level))
                    break
        
        return chapters
    
    def _count_heading_level(self, heading_line: str) -> int:
        """Count heading level by counting # characters at the start."""
        if not heading_line.startswith("#"):
            return 1
        match = re.match(r'^(#+)', heading_line)
        return len(match.group(1)) if match else 1
    
    def split(self, markdown_path: Path, output_dir: Path) -> List[Path]:
        """
        Split markdown file into chapter files.
        Returns list of created chapter file paths.
        """
        with open(markdown_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        chapters = self.detect_chapters(content)
        if len(chapters) <= 1:
            logger.info("No chapter headings detected, skipping split")
            return []
        
        lines = content.splitlines()
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        created_files = []
        for idx, (start_line, heading, level) in enumerate(chapters):
            # Determine end line (next chapter start or end of file)
            end_line = chapters[idx+1][0] if idx+1 < len(chapters) else len(lines)
            
            chapter_content = "\n".join(lines[start_line:end_line])
            # Sanitize heading for filename
            heading_clean = re.sub(r'[^\w\-_\. ]', '', heading)[:50].strip().replace(' ', '_')
            chapter_file = output_dir / f"chapter_{idx+1:03d}_{heading_clean}.md"
            with open(chapter_file, "w", encoding="utf-8") as f:
                f.write(chapter_content)
            created_files.append(chapter_file)
            logger.debug(f"Created chapter: {chapter_file.name}")
        
        return created_files
