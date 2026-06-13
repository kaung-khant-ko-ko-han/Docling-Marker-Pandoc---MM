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
        
        # 1. Broken image references
        if images_dir and images_dir.exists():
            image_links = extract_image_links(content)
            for link in image_links:
                # Resolve relative path relative to markdown's directory
                abs_link = (markdown_path.parent / link).resolve()
                if not abs_link.exists():
                    issues.append(ValidationIssue(
                        type="broken_image",
                        file=str(markdown_path),
                        description=f"Image not found: {link}",
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
    
    def validate_all(self, markdown_files: List[Path], images_dir: Optional[Path] = None) -> List[ValidationReport]:
        """Validate multiple markdown files."""
        return [self.validate_file(f, images_dir) for f in markdown_files]
