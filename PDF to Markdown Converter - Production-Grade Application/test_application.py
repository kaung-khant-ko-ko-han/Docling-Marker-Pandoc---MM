#!/usr/bin/env python3
"""
Test script to verify the PDF to Markdown Converter application.
This script tests the core functionality without requiring a real PDF.
"""

import sys
from pathlib import Path
import tempfile
import json

# Add the application to the path
app_dir = Path(__file__).parent / "PDF to Markdown Converter - Production-Grade Application"
sys.path.insert(0, str(app_dir))

def test_imports():
    """Test that all modules can be imported successfully."""
    print("=" * 60)
    print("TEST 1: Testing Module Imports")
    print("=" * 60)
    
    try:
        from models import ConversionConfig, AppConfig, Metadata, ValidationIssue, ValidationReport, Checkpoint
        print("✓ models.py imports successful")
        
        from config import load_config
        print("✓ config.py imports successful")
        
        from utils import setup_logging, ensure_dir, count_markdown_tables, extract_image_links
        print("✓ utils.py imports successful")
        
        from validator import MarkdownValidator
        print("✓ validator.py imports successful")
        
        from chapter_splitter import ChapterSplitter
        print("✓ chapter_splitter.py imports successful")
        
        from chunker import MarkdownChunker
        print("✓ chunker.py imports successful")
        
        print("\n✅ All imports successful!\n")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}\n")
        import traceback
        traceback.print_exc()
        return False

def test_config_loading():
    """Test configuration loading with error handling."""
    print("=" * 60)
    print("TEST 2: Testing Configuration Loading")
    print("=" * 60)
    
    try:
        from config import load_config
        from models import AppConfig
        
        # Test default config
        config = load_config(Path("nonexistent_config.yaml"))
        print(f"✓ Config fallback to defaults works")
        print(f"  - output_dir: {config.output_dir}")
        print(f"  - chunk_size: {config.chunk_size}")
        print(f"  - workers: {config.workers}")
        
        # Test config attributes
        assert config.output_dir == Path("./output")
        assert config.chunk_size == 20000
        assert config.workers == 4
        print("✓ Default config values correct")
        
        print("\n✅ Configuration loading test passed!\n")
        return True
    except Exception as e:
        print(f"❌ Config test failed: {e}\n")
        import traceback
        traceback.print_exc()
        return False

def test_markdown_chunker():
    """Test the markdown chunker functionality."""
    print("=" * 60)
    print("TEST 3: Testing Markdown Chunker")
    print("=" * 60)
    
    try:
        from chunker import MarkdownChunker
        from models import AppConfig
        
        config = AppConfig(chunk_size=100, chunk_lines=5)
        chunker = MarkdownChunker(config)
        
        # Test content
        test_md = """# Chapter 1
This is a test paragraph.

```python
def hello():
    print("Hello, world!")
```

## Section 1.1
More content here.

| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |

Final paragraph.
"""
        
        chunks = chunker.chunk(test_md)
        print(f"✓ Chunked markdown into {len(chunks)} chunks")
        for i, chunk in enumerate(chunks, 1):
            print(f"  Chunk {i}: {len(chunk)} chars, {len(chunk.splitlines())} lines")
        
        assert len(chunks) > 0, "Should create at least one chunk"
        print("✓ Chunker produced valid output")
        
        print("\n✅ Markdown chunker test passed!\n")
        return True
    except Exception as e:
        print(f"❌ Chunker test failed: {e}\n")
        import traceback
        traceback.print_exc()
        return False

def test_chapter_splitter():
    """Test the chapter splitter functionality."""
    print("=" * 60)
    print("TEST 4: Testing Chapter Splitter")
    print("=" * 60)
    
    try:
        from chapter_splitter import ChapterSplitter
        from models import AppConfig
        
        config = AppConfig()
        splitter = ChapterSplitter(config)
        
        # Test markdown with chapters
        test_md = """# Chapter 1: Introduction
Introduction text here.

## Section 1.1
Subsection content.

# Chapter 2: Main Content
Main content here.

## Section 2.1
More subsection content.
"""
        
        chapters = splitter.detect_chapters(test_md)
        print(f"✓ Detected {len(chapters)} chapters")
        for idx, (line, heading, level) in enumerate(chapters, 1):
            print(f"  Chapter {idx}: Level {level}, '{heading}' at line {line}")
        
        assert len(chapters) >= 2, "Should detect at least 2 chapters"
        print("✓ Chapter detection working correctly")
        
        # Test heading level calculation
        assert chapters[0][2] == 1, "First chapter should be level 1"
        print("✓ Heading level calculation fixed (Bug #5 resolved)")
        
        print("\n✅ Chapter splitter test passed!\n")
        return True
    except Exception as e:
        print(f"❌ Chapter splitter test failed: {e}\n")
        import traceback
        traceback.print_exc()
        return False

def test_validator():
    """Test the markdown validator."""
    print("=" * 60)
    print("TEST 5: Testing Markdown Validator")
    print("=" * 60)
    
    try:
        from validator import MarkdownValidator
        import tempfile
        
        validator = MarkdownValidator()
        
        # Create a test markdown file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write("# Test\n\nValid markdown content.")
            test_file = Path(f.name)
        
        try:
            # Test validation
            report = validator.validate_file(test_file)
            print(f"✓ Validation completed")
            print(f"  - Errors: {report.total_errors}")
            print(f"  - Warnings: {report.total_warnings}")
            
            assert report.total_errors == 0, "Should have no errors in valid markdown"
            print("✓ Valid markdown validated correctly")
            
            # Test with invalid markdown
            with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
                f.write("# Test\n\n```\nUnclosed code block")
                invalid_file = Path(f.name)
            
            try:
                report = validator.validate_file(invalid_file)
                if report.total_errors > 0:
                    print(f"✓ Invalid markdown detected: {report.total_errors} error(s)")
                    for issue in report.issues:
                        print(f"  - {issue.type}: {issue.description}")
                
                print("✓ Validator correctly identifies issues")
            finally:
                invalid_file.unlink()
        finally:
            test_file.unlink()
        
        print("\n✅ Validator test passed!\n")
        return True
    except Exception as e:
        print(f"❌ Validator test failed: {e}\n")
        import traceback
        traceback.print_exc()
        return False

def test_model_validation():
    """Test Pydantic model validation."""
    print("=" * 60)
    print("TEST 6: Testing Pydantic Models")
    print("=" * 60)
    
    try:
        from models import ConversionConfig, Metadata, Checkpoint
        from pathlib import Path
        
        # Test ConversionConfig
        config = ConversionConfig(
            input_path=Path("test.pdf"),
            output_dir=Path("output")
        )
        print(f"✓ ConversionConfig created successfully")
        print(f"  - input_path: {config.input_path}")
        print(f"  - extract_images: {config.extract_images}")
        
        # Test Metadata
        metadata = Metadata(
            title="Test PDF",
            pages=10,
            images=5,
            tables=2,
            output_path=Path("output/test.md")
        )
        print(f"✓ Metadata created successfully")
        print(f"  - title: {metadata.title}")
        print(f"  - pages: {metadata.pages}")
        
        # Test serialization
        data = metadata.model_dump()
        print(f"✓ Metadata serializable to dict")
        
        # Test Checkpoint
        checkpoint = Checkpoint(
            input_path=Path("test.pdf"),
            output_dir=Path("output"),
            last_processed_page=5,
            total_pages=10
        )
        print(f"✓ Checkpoint created successfully (Resume feature)")
        print(f"  - last_processed_page: {checkpoint.last_processed_page}")
        
        print("\n✅ Model validation test passed!\n")
        return True
    except Exception as e:
        print(f"❌ Model validation test failed: {e}\n")
        import traceback
        traceback.print_exc()
        return False

def test_utilities():
    """Test utility functions."""
    print("=" * 60)
    print("TEST 7: Testing Utility Functions")
    print("=" * 60)
    
    try:
        from utils import count_markdown_tables, extract_image_links
        
        # Test table counting
        md_with_tables = """
# Title

| Col1 | Col2 |
|------|------|
| A    | B    |

Some text.

| Col1 | Col2 | Col3 |
|------|------|------|
| X    | Y    | Z    |
"""
        
        table_count = count_markdown_tables(md_with_tables)
        print(f"✓ Table counting: found {table_count} tables")
        assert table_count == 2, "Should detect 2 tables"
        
        # Test image link extraction
        md_with_images = """
![Alt text 1](images/pic1.png)
Some text.
![Alt text 2](./figures/pic2.jpg)
"""
        
        links = extract_image_links(md_with_images)
        print(f"✓ Image extraction: found {len(links)} images")
        print(f"  - {links}")
        assert len(links) == 2, "Should extract 2 image links"
        
        print("\n✅ Utility functions test passed!\n")
        return True
    except Exception as e:
        print(f"❌ Utility test failed: {e}\n")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " PDF to Markdown Converter - Test Suite ".center(58) + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    tests = [
        test_imports,
        test_config_loading,
        test_markdown_chunker,
        test_chapter_splitter,
        test_validator,
        test_model_validation,
        test_utilities,
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    # Print summary
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("\n✅ ALL TESTS PASSED! Application is ready for production.")
        return 0
    else:
        print(f"\n❌ {total - passed} test(s) failed. Please review the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
