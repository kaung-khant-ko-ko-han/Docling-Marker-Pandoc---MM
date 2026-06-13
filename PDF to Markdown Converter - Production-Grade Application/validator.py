"""Quality validation for generated markdown files."""

import re
from pathlib import Path
from typing import List, Optional
import logging

from .models import ValidationIssue, ValidationReport
from .utils import extract_image_links

logger = logging.getLogger(__name__)


class MarkdownValidator:
    """Validate markdown for common issues."""
    
    def validate_file(self, markdown_path: Path, images_dir: Optional[Path] = None) -> ValidationReport:
        """
        Validate a markdown file.
        If images_dir provided, check that image links point to existing files.
        """
        with open(markdown_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        issues = []
        
        # 1. Broken image references (SAFER)
        if images_dir and images_dir.exists():
            image_links = extract_image_links(content)
            for link in image_links:
                resolved = self._safe_resolve_image(markdown_path, link, images_dir)
                if resolved is None and link:  # Only report if link is non-empty
                    issues.append(ValidationIssue(
                        type="broken_image",
                        file=str(markdown_path),
                        description=f"Image not found or unsafe path: {link}",
                        severity="error"
                    ))
        
        # 2. Unclosed code blocks
        code_fences = re.findall(r"```", content)
        if len(code_fences) % 2 != 0:
            issues.append(ValidationIssue(
                type="unclosed_code_block",
                file=str(markdown_path),
                description="Odd number of code fences, likely unclosed block",
                severity="error"
            ))
        
        # 3. Unclosed math blocks ($$)
        math_fences = re.findall(r"\$\$", content)
        if len(math_fences) % 2 != 0:
            issues.append(ValidationIssue(
                type="unclosed_math_block",
                file=str(markdown_path),
                description="Odd number of $$ math delimiters",
                severity="error"
            ))
        
        # 4. Corrupted tables: simple heuristic: lines with | but inconsistent separator counts
        lines = content.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("|") and "|" in line:
                # Check if next line is a separator row (|---|)
                if i+1 < len(lines) and "|" in lines[i+1] and re.search(r"\|[\s\-:]+\|", lines[i+1]):
                    sep_cols = lines[i+1].count("|") - 1
                    data_cols = line.count("|") - 1
                    if sep_cols != data_cols:
                        issues.append(ValidationIssue(
                            type="corrupted_table",
                            file=str(markdown_path),
                            line=i+1,
                            description=f"Table column mismatch: header {data_cols}, separator {sep_cols}",
                            severity="warning"
                        ))
        
        # 5. Empty lines in code block? Not strictly an error.
        
        errors = [i for i in issues if i.severity == "error"]
        warnings = [i for i in issues if i.severity == "warning"]
        
        return ValidationReport(
            issues=issues,
            total_errors=len(errors),
            total_warnings=len(warnings),
            markdown_file=str(markdown_path)
        )
    
    def _safe_resolve_image(self, markdown_path: Path, link: str, base_dir: Path) -> Optional[Path]:
        """Safely resolve image path within base directory."""
        try:
            # Resolve relative to markdown file
            target = (markdown_path.parent / link).resolve()
            # Ensure target is within expected bounds (prevent directory traversal)
            target_str = str(target)
            base_str = str(base_dir.resolve())
            if not (target_str.startswith(base_str) or target_str.startswith(str(markdown_path.parent.resolve()))):
                logger.warning(f"Unsafe image path detected: {link}")
                return None
            return target if target.exists() else None
        except (OSError, ValueError, RuntimeError) as e:
            logger.debug(f"Error resolving image path {link}: {e}")
            return None
    
    def validate_all(self, markdown_files: List[Path], images_dir: Optional[Path] = None) -> List[ValidationReport]:
        """Validate multiple markdown files."""
        return [self.validate_file(f, images_dir) for f in markdown_files]
