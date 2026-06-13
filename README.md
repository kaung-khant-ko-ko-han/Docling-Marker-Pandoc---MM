# Docling-Marker-Pandoc---MM


PDF / EPUB / DOCX စာအုပ်တွေကို Markdown ပြောင်းဖို့ဆိုရင် **Docling + Marker + Pandoc** ကို ပေါင်းသုံးတဲ့ Workflow က အကောင်းဆုံးတွေထဲက တစ်ခုပါ။

## Tool တစ်ခုချင်းစီရဲ့ အခန်းကဏ္ဍ

### 1. Docling

IBM က ဖန်တီးထားတဲ့ Document AI Framework ဖြစ်ပါတယ်။

**အားသာချက်**

* PDF → Markdown
* PDF → JSON
* PDF → HTML
* OCR Support
* Table Extraction
* Figure Detection
* Layout Analysis

**သင့်တော်သော File**

* Technical PDF
* Research Paper
* Manual
* Documentation

---

### 2. Marker

AI-based PDF → Markdown Converter ဖြစ်ပါတယ်။

**အားသာချက်**

* Formula (LaTeX) ထိန်းနိုင်
* Table ထိန်းနိုင်
* Multi-column PDF ကောင်း
* Diagram Caption တွေ ထိန်းနိုင်

**သင့်တော်သော File**

* Textbook
* Scientific Book
* Engineering Book

---

### 3. Pandoc

Document Conversion King လို့ ခေါ်ကြပါတယ်။

**Convert**

* EPUB ↔ Markdown
* DOCX ↔ Markdown
* HTML ↔ Markdown
* PDF (Indirect)

---

# Recommended Architecture

```text
PDF
 │
 ├── Technical PDF
 │      ↓
 │   Docling
 │      ↓
 │   Markdown
 │
 └── Textbook PDF
        ↓
      Marker
        ↓
     Markdown

Markdown
    ↓
Translation Pipeline
    ↓
Markdown (Myanmar)

Markdown
    ↓
Pandoc
    ↓
EPUB / DOCX / PDF
```

---

# Installation

## Python Environment

```bash
python -m venv venv

source venv/bin/activate
```

Windows

```cmd
venv\Scripts\activate
```

---

# Install Docling

```bash
pip install docling
```

စမ်းသပ်

```bash
docling --help
```

---

# Install Marker

Official Project:

[Marker GitHub](https://github.com/datalab-to/marker?utm_source=chatgpt.com)

Install

```bash
pip install marker-pdf
```

GPU ရှိရင်

```bash
pip install torch torchvision
```

---

# Install Pandoc

Official:

[Pandoc Official Website](https://pandoc.org?utm_source=chatgpt.com)

Windows

```bash
winget install Pandoc.Pandoc
```

Linux

```bash
sudo apt install pandoc
```

Check

```bash
pandoc --version
```

---

# Method 1 — Docling → Markdown

PDF တစ်ခု

```bash
docling mybook.pdf
```

Output

```text
mybook/
 ├─ document.md
 ├─ images/
 ├─ tables/
 └─ metadata.json
```

---

Output Folder သတ်မှတ်

```bash
docling mybook.pdf \
    --output output
```

---

# Method 2 — Marker → Markdown

```bash
marker_single mybook.pdf output/
```

Output

```text
output/
 ├─ mybook.md
 ├─ images/
 └─ metadata.json
```

---

# EPUB → Markdown

Pandoc သုံး

```bash
pandoc book.epub \
    -t markdown \
    -o book.md
```

---

# DOCX → Markdown

```bash
pandoc book.docx \
    -t markdown \
    -o book.md
```

---

# HTML → Markdown

```bash
pandoc book.html \
    -t markdown \
    -o book.md
```

---

# Markdown → EPUB

ဘာသာပြန်ပြီး ပြန်ထုတ်ချင်ရင်

```bash
pandoc book_mm.md \
    -o book_mm.epub
```

---

# Markdown → DOCX

```bash
pandoc book_mm.md \
    -o book_mm.docx
```

---

# Markdown → PDF

```bash
pandoc book_mm.md \
    -o book_mm.pdf
```

---

# 500–2000 Page Technical Book အတွက် Recommended Workflow

```text
PDF
 │
 ▼
Marker
 │
 ▼
Markdown
 │
 ▼
Chunking
 │
 ▼
AI Translation
 │
 ▼
QA Validation
 │
 ▼
Merged Markdown
 │
 ▼
Pandoc
 │
 ├─ EPUB
 ├─ DOCX
 └─ PDF
```

---

# သင့်လို Technical Book 500–2000 Pages ဘာသာပြန် Project အတွက်

အကောင်းဆုံး Workflow က

```text
EPUB
  ↓
Pandoc
  ↓
Markdown

PDF
  ↓
Marker
  ↓
Markdown

Markdown
  ↓
Chunking
  ↓
AI Translation
  ↓
Validation
  ↓
Pandoc
  ↓
EPUB / DOCX / PDF
```

ဒီ Workflow က Formula, Table, Image Reference, Heading Structure, TOC (မာတိကာ) တွေ မပျက်ဘဲ AI Translation Pipeline ထဲ ထည့်နိုင်တဲ့ Production-Grade Workflow ဖြစ်ပါတယ်။
