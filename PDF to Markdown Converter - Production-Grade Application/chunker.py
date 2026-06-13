"""Split markdown into chunks suitable for LLM translation."""

import re
from pathlib import Path
from typing import List, Iterator
import logging

from .models import AppConfig

logger = logging.getLogger(__name__)


class MarkdownChunker:
    """Smart markdown chunker preserving code blocks, tables, and equations."""
    
    def __init__(self, config: AppConfig):
        self.max_chars = config.chunk_size
        self.max_lines = config.chunk_lines
    
    def _is_code_fence(self, line: str) -> bool:
        return line.strip().startswith("```")
    
    def _is_math_block(self, line: str) -> bool:
        return line.strip().startswith("$$")
    
    def _is_table_line(self, line: str) -> bool:
        return line.strip().startswith("|") and "|" in line
    
    def chunk(self, markdown_text: str) -> List[str]:
        """
        Split markdown into chunks while respecting markdown syntax.
        Returns list of chunk strings.
        """
        lines = markdown_text.splitlines()
        chunks = []
        current_chunk = []
        current_size = 0
        
        in_code_block = False
        in_math_block = False
        in_table = False
        
        for line in lines:
            line_len = len(line) + 1  # +1 for newline
            
            # Check state transitions
            if not in_code_block and self._is_code_fence(line):
                in_code_block = True
            elif in_code_block and self._is_code_fence(line):
                in_code_block = False
            elif not in_math_block and self._is_math_block(line):
                in_math_block = True
            elif in_math_block and self._is_math_block(line):
                in_math_block = False
            elif not in_table and self._is_table_line(line):
                in_table = True
            elif in_table and not line.strip():
                in_table = False
            
            # If adding this line exceeds limit AND we are not in a protected block,
            # and we have some content, then finalize chunk
            if (current_size + line_len > self.max_chars and 
                not in_code_block and not in_math_block and not in_table and
                current_chunk):
                chunks.append("\n".join(current_chunk))
                current_chunk = []
                current_size = 0
            
            current_chunk.append(line)
            current_size += line_len
        
        # Add last chunk
        if current_chunk:
            chunks.append("\n".join(current_chunk))
        
        # Fallback: if any chunk exceeds max_lines, hard split by lines (FIXED)
        final_chunks = []
        for chunk in chunks:
            lines_in_chunk = len(chunk.splitlines())  # More reliable than counting '\n'
            if lines_in_chunk > self.max_lines:
                # Hard split by lines
                sub_lines = chunk.splitlines()
                for i in range(0, len(sub_lines), self.max_lines):
                    sub_chunk = "\n".join(sub_lines[i:i+self.max_lines])
                    final_chunks.append(sub_chunk)
            else:
                final_chunks.append(chunk)
        
        return final_chunks
    
    def chunk_file(self, markdown_path: Path, output_dir: Path, prefix: str = "chunk") -> List[Path]:
        """Chunk a markdown file and write chunks to output_dir."""
        with open(markdown_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        chunks = self.chunk(content)
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        chunk_files = []
        for idx, chunk_text in enumerate(chunks):
            chunk_file = output_dir / f"{prefix}_{idx+1:04d}.md"
            with open(chunk_file, "w", encoding="utf-8") as f:
                f.write(chunk_text)
            chunk_files.append(chunk_file)
        
        logger.info(f"Created {len(chunks)} chunks from {markdown_path.name}")
        return chunk_files
