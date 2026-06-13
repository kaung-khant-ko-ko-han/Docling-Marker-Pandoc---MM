# PDF to Markdown Converter (Marker-based)

Production-grade tool to convert PDF books, technical documents, and research papers into high-quality Markdown, optimized for AI translation pipelines.

## Features

- **Single & batch conversion** of PDFs
- **Preserves** headings, tables, math (LaTeX), images, lists, code blocks, footnotes, captions, multi-column layouts
- **Automatic chapter detection** and splitting into separate files
- **Metadata extraction** (title, author, pages, language, counts)
- **Image extraction** and link updating
- **LLM‑ready chunking** (configurable size, respects markdown syntax)
- **Quality validation** (broken links, unclosed blocks, corrupted tables)
- **Resume capability** for large documents (checkpoints every N pages)
- **Parallel processing** for batch jobs
- **YAML configuration** & CLI overrides

## Installation

```bash
# Clone or create project directory
pip install -r requirements.txt
