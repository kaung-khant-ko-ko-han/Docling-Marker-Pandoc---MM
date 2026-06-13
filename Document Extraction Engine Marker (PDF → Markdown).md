Marker ကို PDF → Markdown ပြောင်းဖို့ပဲ မသုံးသင့်ပါဘူး။ Technical Book Translation Pipeline တစ်ခုလုံးရဲ့ **Document Extraction Engine** အနေနဲ့ သုံးသင့်ပါတယ်။

---

# Marker ဆိုတာ ဘာလဲ

Marker သည် PDF ကို AI ဖြင့် Analyze လုပ်ပြီး Markdown ထုတ်ပေးသော Open Source Tool ဖြစ်ပါတယ်။

သူ့ရဲ့ အဓိက Feature က

```text
PDF
 ↓
Layout Detection
 ↓
OCR
 ↓
Table Recognition
 ↓
Formula Detection
 ↓
Image Extraction
 ↓
Markdown
```

ဖြစ်ပါတယ်။

---

# Marker က ဘာတွေ Extract လုပ်နိုင်လဲ

## Headings

PDF

```text
Chapter 1
Introduction to Control Systems
```

Markdown

```markdown
# Chapter 1

## Introduction to Control Systems
```

---

## Lists

PDF

```text
1. Sensor
2. Controller
3. Actuator
```

Markdown

```markdown
1. Sensor
2. Controller
3. Actuator
```

---

## Tables

PDF

```text
Voltage Current
12V     2A
24V     5A
```

Markdown

```markdown
| Voltage | Current |
|----------|----------|
| 12V | 2A |
| 24V | 5A |
```

---

## Formulas

PDF

```text
F = ma
```

Markdown

```markdown
$$
F = ma
$$
```

---

## Images

PDF

```text
Figure 1. Motor Driver
```

Output

```text
images/
 ├─ fig_001.png
 ├─ fig_002.png
```

Markdown

```markdown
![Figure 1](images/fig_001.png)
```

---

# Installation

## CPU Only

```bash
pip install marker-pdf
```

---

## GPU

NVIDIA GPU ရှိရင်

```bash
pip install marker-pdf

pip install torch torchvision
```

---

# Basic Usage

PDF တစ်ခု

```bash
marker_single book.pdf output/
```

Output

```text
output/

 ├── book.md
 ├── images/
 ├── metadata.json
```

---

# Folder တစ်ခုလုံး

```bash
marker folder/
```

ဥပမာ

```text
books/

 ├── book1.pdf
 ├── book2.pdf
 ├── book3.pdf
```

Run

```bash
marker books/
```

---

# Output Structure

```text
output/

 ├── book.md
 ├── images/
 │     ├── fig1.png
 │     ├── fig2.png
 │
 ├── metadata.json
 │
 └── tables/
```

---

# metadata.json

အထဲမှာ

```json
{
  "title": "Control Systems Engineering",
  "author": "Nise",
  "pages": 842
}
```

လိုမျိုး ပါလာတတ်ပါတယ်။

---

# Large Textbook (500–2000 Pages)

ဥပမာ

```text
Artificial Intelligence
2000 pages
```

ကို

```bash
marker_single ai_book.pdf output/
```

Run လိုက်ရင်

```text
output/

 ├── ai_book.md
 ├── images/
 └── metadata.json
```

ရလာမယ်။

---

# Marker Output ကို AI Translation အတွက် မတိုက်ရိုက်ပို့သင့်

အကြောင်းက

```text
2000 pages
=
4~8 million characters
```

ရှိနိုင်လို့ဖြစ်ပါတယ်။

ဒါကြောင့်

```text
PDF
 ↓
Marker
 ↓
Markdown
 ↓
Chunking
 ↓
Translation
 ↓
Merge
```

လုပ်ရပါတယ်။

---

# Recommended Chunk Size

AI Translation အတွက်

```text
500 ~ 1500 lines
```

သို့မဟုတ်

```text
20k ~ 50k characters
```

စီ ခွဲသင့်ပါတယ်။

---

# Chapter Split

Markdown ထဲက

```markdown
# Chapter 1

# Chapter 2

# Chapter 3
```

ကို ရှာပြီး

```text
chapter_01.md
chapter_02.md
chapter_03.md
```

ခွဲထားတာ အကောင်းဆုံးပါ။

Technical Book ဘာသာပြန်တဲ့အခါ Chapter အလိုက် ခွဲပြီး AI ကို ပို့ရင် Heading Structure, TOC, Formula, Table တွေ မပျက်ဘဲ ပြန်ထွက်လာနိုင်ပါတယ်။

---

# သင့်အတွက် အကောင်းဆုံး Production Workflow

```text
PDF
 ↓
Marker
 ↓
Markdown

Markdown
 ↓
Chapter Split

chapter_01.md
chapter_02.md
chapter_03.md

 ↓
AI Translation

chapter_01_mm.md
chapter_02_mm.md
chapter_03_mm.md

 ↓
Merge

book_mm.md

 ↓
Pandoc

book_mm.epub
book_mm.docx
book_mm.pdf
```

500–2000 Pages Engineering / Robotics / AI / Control Systems Textbook များကို ဘာသာပြန်မယ်ဆိုရင် Marker ကို PDF Extraction Engine အဖြစ် သုံးပြီး Chapter Split → Translation → QA Validation → Pandoc Export Workflow နဲ့ သွားတာက အထိရောက်ဆုံး ဖြစ်ပါတယ်။
