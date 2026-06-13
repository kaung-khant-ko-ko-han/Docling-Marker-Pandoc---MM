"""
PDF မှ Markdown သို့ အသွင်းပြောင်းသည့် အစီအစဥ်မြူပ်မုံရံု

ဤအပ်လီကေးရှင်းသည် PDF ឯកសារမှ Markdown ပုံစံသို့ အသွင်းပြောင်းသည့်ကိရိယာတစ်ခုဖြစ်သည်။
Marker လိုင်ဘ်ररီကို အသုံးပြု၍ အခန်းခွဲခြင်း၊ ဘာသာစကားပြန်ဆိုမှုအတွက် အပိုင်းခွဲခြင်း၊ 
ပုံတွေထုတ်ယူခြင်း၊ နှင့် အရည်အသွေးအတည်ပြုခြင်းတွေကို ပါဝင်သည်။
"""

__version__ = "1.0.0"
__author__ = "Kaung Khant Ko Ko Han"

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
