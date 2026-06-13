```markdown
<p align="center">
  <img src="data/images/datalab-logo.png" alt="Datalab Logo" width="150"/>
</p>
<h1 align="center">Datalab</h1>
<p align="center">
  <strong>State of the Art models for Document Intelligence</strong>
</p>
<p align="center">
  <a href="https://www.gnu.org/licenses/gpl-3.0.html"><img src="https://img.shields.io/badge/Code%20License-GPL--3.0-green.svg" alt="Code License"></a>
  <a href="https://www.datalab.to/pricing"><img src="https://img.shields.io/badge/Model%20License-OpenRAIL--M-blue.svg" alt="Model License"></a>
  <a href="https://discord.gg/KuZwXNGnfH"><img src="https://img.shields.io/badge/Discord-Join%20us-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
</p>
<p align="center">
  <a href="https://www.datalab.to"><img src="https://img.shields.io/badge/Homepage-datalab.to-blue" alt="Homepage"></a>
  <a href="https://documentation.datalab.to"><img src="https://img.shields.io/badge/Docs-Read%20the%20docs-blue" alt="Docs"></a>
  <a href="https://www.datalab.to/playground"><img src="https://img.shields.io/badge/Playground-Try%20it-orange" alt="Public Playground"></a>
</p>

<hr/>

# Marker (မာကာ)

Marker သည် PDF၊ ပုံ၊ PPTX၊ DOCX၊ XLSX၊ HTML၊ EPUB ဖိုင်များကို markdown၊ JSON၊ chunks နှင့် HTML အဖြစ်သို့ လျင်မြန်တိကျစွာ ပြောင်းလဲပေးသည်။

- ဘာသာစကားအားလုံးဖြင့် PDF၊ ပုံ၊ PPTX၊ DOCX၊ XLSX၊ HTML၊ EPUB ဖိုင်များကို ပြောင်းလဲပေးသည်
- ဇယားများ (table)၊ ဖောင်များ (form)၊ ညီမျှခြင်းများ (equation)၊ စာကြောင်းတွင်းသင်္ချာ (inline math)၊ လင့်ခ်များ (link)၊ ကိုးကားချက်များ (reference) နှင့် ကုဒ်တုံးများ (code block) ကို ပုံစံချပေးသည်
- ရုပ်ပုံများကို ထုတ်ယူသိမ်းဆည်းပေးသည်
- ခေါင်းညွှန်း (header) / အောက်ခြေညွှန်း (footer) / အခြားအပိုပစ္စည်းများကို ဖယ်ရှားပေးသည်
- သင့်ကိုယ်ပိုင်ပုံစံချခြင်းနှင့် ယုတ္တိဖြင့် တိုးချဲ့နိုင်သည်
- JSON schema (beta) ပေးထားပါက ဖွဲ့စည်းတည်ဆောက်ပုံဆိုင်ရာ ထုတ်ယူမှု (structured extraction) ကို ပြုလုပ်ပေးသည်
- စိတ်ကြိုက် LLMs များဖြင့် တိကျမှုကို မြှင့်တင်နိုင်သည် (နှင့် သင့်ကိုယ်ပိုင် prompt)
- GPU၊ CPU (သို့) MPS ပေါ်တွင် အလုပ်လုပ်သည်

## Datalab ၏ စီမံခန့်ခွဲထားသော Platform (Managed Platform) ကို စမ်းသုံးပါ

ကျွန်ုပ်တို့၏ စီမံခန့်ခွဲထားသော platform သည် ကျွန်ုပ်တို့၏ နောက်ဆုံးပေါ် open source မော်ဒယ် [Chandra](https://github.com/datalab-to/chandra) ကို အသုံးပြုသည် — ၎င်းသည် Marker ထက် တိကျမှုပိုမိုမြင့်မားပြီး၊ မူရင်းအတိုင်း ဒေတာထိန်းသိမ်းမှုမရှိ (zero data retention)၊ SOC 2 Type 2 နှင့် စိတ်ကြိုက် BAAs များပါရှိသည်။

ပမာဏမြင့်မားသော အလုပ်များရှိပါက၊ တစ်ပတ်လျှင် စာမျက်နှာ ၂၀၀ သန်းကျော် လုပ်ဆောင်ပြီးဖြစ်သော batch processing service ကို ကျွန်ုပ်တို့ ကမ်းလှမ်းထားသည် — သင့်အလုပ်များ သတ်မှတ်ချိန်အတွင်း ပြီးစီးစေရန် အခြေခံအဆောက်အအုံကို ကျွန်ုပ်တို့ စီမံပေးပါသည်။

**အခမဲ့ ခရက်ဒစ် $5** ဖြင့် စတင်လိုက်ပါ — [sign up](https://www.datalab.to/?utm_source=gh-marker) — စက္ကန့် ၃၀ အတွင်း ပြီးမည် — (သို့) ကျွန်ုပ်တို့၏ [public playground](https://www.datalab.to/playground?utm_source=gh-marker) ကို စမ်းသုံးကြည့်ပါ။

စီးပွားဖြစ် ကိုယ်တိုင် hosting ပြုလုပ်ရန် လိုင်စင် လိုအပ်သည် — [Commercial usage](#commercial-usage) ကို ကြည့်ပါ။ on-prem လိုင်စင်အတွက် [ကျွန်ုပ်တို့ကို ဆက်သွယ်ပါ](https://www.datalab.to/contact?utm_source=gh-marker-onprem)။

## စွမ်းဆောင်ရည် (Performance)

<img src="data/images/overall.png" width="800px"/>

Marker သည် Llamaparse နှင့် Mathpix ကဲ့သို့ cloud ဝန်ဆောင်မှုများအပြင် အခြား open source ကိရိယာများနှင့် ယှဉ်လျှင် အဆင်ပြေသော ရလဒ်များ ပြသသည်။

အထက်ပါ ရလဒ်များသည် PDF စာမျက်နှာတစ်ခုချင်းစီကို အစဉ်လိုက် (serially) run ခြင်းဖြစ်သည်။ Marker သည် batch mode တွင် run ပါက သိသိသာသာ ပိုမိုမြန်ဆန်ပြီး H100 တစ်လုံးတွင် တစ်စက္ကန့်လျှင် စာမျက်နှာ ၂၅ မျက်နှာ ထွက်ရှိနိုင်သည်။

အသေးစိတ် အမြန်နှုန်းနှင့် တိကျမှု စံညွှန်းများ (benchmarks) နှင့် သင့်ကိုယ်ပိုင် စံညွှန်းများ မည်သို့ run ရမည်ကို [အောက်တွင်](#benchmarks) ကြည့်ပါ။

## Hybrid Mode (ပေါင်းစပ် Mode)

အမြင့်ဆုံးတိကျမှုအတွက် `--use_llm` flag ကို သုံး၍ marker နှင့်အတူ LLM ကို အသုံးပြုပါ။ ၎င်းသည် စာမျက်နှာများကိုဖြတ်၍ ဇယားများ ပေါင်းစည်းခြင်း၊ စာကြောင်းတွင်းသင်္ချာ (inline math) ကို ကိုင်တွယ်ခြင်း၊ ဇယားများကို စနစ်တကျ ပုံစံချခြင်းနှင့် ဖောင်များမှ တန်ဖိုးများ ထုတ်ယူခြင်းတို့ကို လုပ်ဆောင်ပေးလိမ့်မည်။ ၎င်းသည် gemini (သို့) ollama မော်ဒယ် မည်သည်ကိုမဆို အသုံးပြုနိုင်သည်။ မူရင်းအားဖြင့် `gemini-2.0-flash` ကို သုံးသည်။ အသေးစိတ်အတွက် [အောက်တွင်](#llm-services) ကြည့်ပါ။

ဤသည်မှာ marker၊ gemini flash တစ်ခုတည်း နှင့် marker + use_llm တို့ကို နှိုင်းယှဉ်ထားသော ဇယား (table) စံညွှန်း ဖြစ်သည်-

<img src="data/images/table.png" width="400px"/>

သင်မြင်ရသည့်အတိုင်း use_llm mode သည် marker သို့မဟုတ် gemini တစ်ခုတည်းထက် တိကျမှု ပိုမိုမြင့်မားသည်။

## နမူနာများ (Examples)

| PDF | ဖိုင်အမျိုးအစား | Markdown                                                                                                                     | JSON                                                                                                   |
|-----|-----------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [Think Python](https://greenteapress.com/thinkpython/thinkpython.pdf) | ဖတ်စာအုပ် | [ကြည့်ရန်](https://github.com/VikParuchuri/marker/blob/master/data/examples/markdown/thinkpython/thinkpython.md)                 | [ကြည့်ရန်](https://github.com/VikParuchuri/marker/blob/master/data/examples/json/thinkpython.json)         |
| [Switch Transformers](https://arxiv.org/pdf/2101.03961.pdf) | arXiv စာတမ်း | [ကြည့်ရန်](https://github.com/VikParuchuri/marker/blob/master/data/examples/markdown/switch_transformers/switch_trans.md) | [ကြည့်ရန်](https://github.com/VikParuchuri/marker/blob/master/data/examples/json/switch_trans.json) |
| [Multi-column CNN](https://arxiv.org/pdf/1804.07821.pdf) | arXiv စာတမ်း | [ကြည့်ရန်](https://github.com/VikParuchuri/marker/blob/master/data/examples/markdown/multicolcnn/multicolcnn.md)                 | [ကြည့်ရန်](https://github.com/VikParuchuri/marker/blob/master/data/examples/json/multicolcnn.json)         |

# စီးပွားဖြစ်အသုံးပြုမှု (Commercial usage)

ကျွန်ုပ်တို့၏ မော်ဒယ် အလေးချိန်များ (model weights) သည် ပြုပြင်ထားသော AI Pubs Open Rail-M လိုင်စင်ကို အသုံးပြုသည် (သုတေသန၊ ကိုယ်ရေးကိုယ်တာအသုံးပြုမှုနှင့် ရန်ပုံငွေ/ဝင်ငွေ $2M အောက် startup များအတွက် အခမဲ့) နှင့် ကျွန်ုပ်တို့၏ ကုဒ်သည် GPL ဖြစ်သည်။ ပိုမိုကျယ်ပြန့်သော စီးပွားဖြစ်လိုင်စင်အတွက် (သို့) GPL လိုအပ်ချက်များကို ဖယ်ရှားရန်အတွက် ကျွန်ုပ်တို့၏ pricing page [ဤနေရာ](https://www.datalab.to/pricing?utm_source=gh-marker) တွင် ဝင်ရောက်ကြည့်ရှုပါ။

# အသိုင်းအဝိုင်း (Community)

[Discord](https://discord.gg//KuZwXNGnfH) တွင် ကျွန်ုပ်တို့သည် အနာဂတ်ဖွံ့ဖြိုးတိုးတက်ရေးကို ဆွေးနွေးကြသည်။

# တပ်ဆင်ခြင်း (Installation)

သင့်တွင် python 3.10+ နှင့် [PyTorch](https://pytorch.org/get-started/locally/) ရှိရန် လိုအပ်သည်။

အောက်ပါအတိုင်း တပ်ဆင်ပါ-

```shell
pip install marker-pdf
```

အကယ်၍ သင်သည် PDF များမှလွဲ၍ အခြားစာရွက်စာတမ်းများပေါ်တွင် marker ကို အသုံးပြုလိုပါက အောက်ပါအတိုင်း နောက်ထပ် dependencies များ တပ်ဆင်ရန် လိုအပ်သည်-

```shell
pip install marker-pdf[full]
```

# အသုံးပြုခြင်း (Usage)

ပထမဦးစွာ ဖွဲ့စည်းမှုအချို့-

- သင်၏ torch device ကို အလိုအလျောက် ရှာဖွေတွေ့ရှိမည်၊ သို့သော် သင်က ၎င်းကို override လုပ်နိုင်သည်။ ဥပမာ `TORCH_DEVICE=cuda` ။
- အချို့ PDF များသည် ဒစ်ဂျစ်တယ်ဖြစ်သော်လည်း စာသားအရည်အသွေးညံ့သည်။ မျဉ်းကြောင်းအားလုံးပေါ်တွင် OCR ကို အတင်းအကြပ်လုပ်ရန် `--force_ocr` ကို သတ်မှတ်ပါ၊ (သို့) ဒစ်ဂျစ်တယ်စာသားအားလုံးကို ထိန်းသိမ်းပြီး ရှိပြီးသား OCR စာသားကို ဖယ်ရှားရန် `strip_existing_ocr` ကို သတ်မှတ်ပါ။
- စာကြောင်းတွင်းသင်္ချာ (inline math) ကို ဂရုစိုက်ပါက inline math ကို LaTeX သို့ ပြောင်းရန် `force_ocr` ကို သတ်မှတ်ပါ။

## အပြန်အလှန်တုံ့ပြန်နိုင်သော အက်ပ် (Interactive App)

ကျွန်ုပ်တို့သည် streamlit အက်ပ်တစ်ခုကို ထည့်သွင်းထားပြီး၊ အခြေခံရွေးစရာအချို့ဖြင့် marker ကို အပြန်အလှန်တုံ့ပြန်စမ်းကြည့်နိုင်သည်။ အောက်ပါအတိုင်း run ပါ-

```shell
pip install streamlit streamlit-ace
marker_gui
```

## ဖိုင်တစ်ခုတည်းကို ပြောင်းလဲခြင်း (Convert a single file)

```shell
marker_single /path/to/file.pdf
```

သင်သည် PDF (သို့) ပုံများကို ထည့်သွင်းနိုင်သည်။

ရွေးစရာများ (Options):
- `--page_range TEXT` : မည်သည့်စာမျက်နှာများ လုပ်ဆောင်ရမည်ကို သတ်မှတ်ပါ။ comma ခြားထားသော စာမျက်နှာနံပါတ်များနှင့် အကွာအဝေးများကို လက်ခံသည်။ ဥပမာ: `--page_range "0,5-10,20"` သည် စာမျက်နှာ 0၊ 5 မှ 10 အထိ၊ နှင့် စာမျက်နှာ 20 ကို လုပ်ဆောင်မည်။
- `--output_format [markdown|json|html|chunks]` : ရလဒ်များအတွက် ဖော်မတ်ကို သတ်မှတ်ပါ။
- `--output_dir PATH` : output ဖိုင်များ သိမ်းဆည်းမည့် လမ်းညွှန်။ မူရင်းအားဖြင့် settings.OUTPUT_DIR ရှိ တန်ဖိုးကို သုံးသည်။
- `--paginate_output` : output ကို စာမျက်နှာခွဲပြီး၊ `\n\n{PAGE_NUMBER}` နောက်တွင် `-` * 48 ပြီးနောက် `\n\n` ထည့်ပေးသည်။
- `--use_llm` : တိကျမှုမြှင့်တင်ရန် LLM ကို အသုံးပြုသည်။ LLM backend ကို configure လုပ်ရန် လိုအပ်သည် - [အောက်တွင်](#llm-services) ကြည့်ပါ။
- `--force_ocr` : စာသားထုတ်ယူနိုင်သော စာမျက်နှာများအတွက်ပင် စာရွက်စာတမ်းတစ်ခုလုံးပေါ်တွင် OCR လုပ်ဆောင်ခြင်းကို အတင်းအကြပ်လုပ်ပါ။ ၎င်းသည် inline math ကိုလည်း စနစ်တကျ ပုံစံချပေးမည်။
- `--block_correction_prompt` : LLM mode သက်ဝင်နေပါက၊ marker ၏ output ကို ပြင်ဆင်ရန် အသုံးပြုမည့် optional prompt တစ်ခု။ ၎င်းသည် သင်အသုံးပြုလိုသော စိတ်ကြိုက် ပုံစံချခြင်း (သို့) ယုတ္တိအတွက် အသုံးဝင်သည်။
- `--strip_existing_ocr` : စာရွက်စာတမ်းရှိ ရှိပြီးသား OCR စာသားအားလုံးကို ဖယ်ရှားပြီး surya ဖြင့် ပြန်လည် OCR လုပ်ပါ။
- `--redo_inline_math` : အမြင့်ဆုံးအရည်အသွေးရှိသော inline math ပြောင်းလဲခြင်းကို လိုချင်ပါက ၎င်းကို `--use_llm` နှင့်အတူ သုံးပါ။
- `--disable_image_extraction` : PDF မှ ရုပ်ပုံများကို မထုတ်ယူပါနှင့်။ `--use_llm` ကိုလည်း သတ်မှတ်ပါက၊ ရုပ်ပုံများကို ဖော်ပြချက်ဖြင့် အစားထိုးမည်။
- `--debug` : နောက်ထပ် logging နှင့် ရောဂါရှာဖွေရေးအချက်အလက်များအတွက် debug mode ကို ဖွင့်ပါ။
- `--processors TEXT` : ပုံသေ processors များကို override လုပ်ရန် ၎င်းတို့၏ full module paths များကို comma ခြားပြီး ပေးပါ။ ဥပမာ: `--processors "module1.processor1,module2.processor2"`
- `--config_json PATH` : နောက်ထပ် ဆက်တင်များပါဝင်သော JSON configuration file တစ်ခု၏ လမ်းညွှန်။
- `config --help` : ရရှိနိုင်သော builder များ၊ processor များနှင့် converter များနှင့် ၎င်းတို့၏ ဆက်စပ် configuration များကို စာရင်းပြုစုပေးသည်။ ဤတန်ဖိုးများကို marker ပုံသေများကို ထပ်မံချိန်ညှိရန်အတွက် JSON configuration file တည်ဆောက်ရန် အသုံးပြုနိုင်သည်။
- `--converter_cls` : `marker.converters.pdf.PdfConverter` (ပုံသေ) (သို့) `marker.converters.table.TableConverter` တစ်ခုခု။ `PdfConverter` သည် PDF တစ်ခုလုံးကို ပြောင်းလဲပေးမည်၊ `TableConverter` သည် ဇယားများကိုသာ ထုတ်ယူပြောင်းလဲပေးမည်။
- `--llm_service` : `--use_llm` ပေးထားပါက မည်သည့် llm service ကို သုံးမည်နည်း။ ၎င်းသည် မူရင်းအားဖြင့် `marker.services.gemini.GoogleGeminiService` ဖြစ်သည်။
- `--help` : marker သို့ ပေးပို့နိုင်သော flag များအားလုံးကို ကြည့်ရှုပါ (အထက်တွင်ဖော်ပြထားသည်ထက် ရွေးစရာများစွာ ထပ်မံပံ့ပိုးသည်)။

surya OCR အတွက် ပံ့ပိုးထားသော ဘာသာစကားများစာရင်းမှာ [ဤနေရာ](https://github.com/VikParuchuri/surya/blob/master/surya/recognition/languages.py) တွင်ဖြစ်သည်။ OCR မလိုအပ်ပါက marker သည် ဘာသာစကားမရွေး အလုပ်လုပ်နိုင်သည်။

## ဖိုင်များစွာကို ပြောင်းလဲခြင်း (Convert multiple files)

```shell
marker /path/to/input/folder
```

- `marker` သည် အထက်ပါ `marker_single` မှ ရွေးစရာများအားလုံးကို ထောက်ပံ့ပေးသည်။
- `--workers` သည် တစ်ပြိုင်နက် run မည့် ပြောင်းလဲရေး လုပ်သားအရေအတွက်ဖြစ်သည်။ ၎င်းကို ပုံသေအားဖြင့် အလိုအလျောက် သတ်မှတ်ပေးသည်၊ သို့သော် သင်က CPU/GPU အသုံးပြုမှု ပိုမိုကုန်ကျစေသော်လည်း throughput ကို မြှင့်တင်ရန် တိုးမြှင့်နိုင်သည်။ Marker သည် အထွတ်အထိပ်တွင် လုပ်သားတစ်ဦးလျှင် VRAM 5GB ကို အသုံးပြုမည်၊ ပျမ်းမျှအားဖြင့် 3.5GB ဖြစ်သည်။

## GPU အများအပြားပေါ်တွင် ဖိုင်များစွာကို ပြောင်းလဲခြင်း (Convert multiple files on multiple GPUs)

```shell
NUM_DEVICES=4 NUM_WORKERS=15 marker_chunk_convert ../pdf_in ../md_out
```

- `NUM_DEVICES` သည် အသုံးပြုမည့် GPU အရေအတွက်ဖြစ်သည်။ `2` (သို့) ထက်ကြီးရမည်။
- `NUM_WORKERS` သည် GPU တစ်ခုစီတွင် run မည့် အပြိုင် လုပ်ငန်းစဉ် အရေအတွက်ဖြစ်သည်။

## python မှ အသုံးပြုခြင်း (Use from python)

`marker/converters/pdf.py` ရှိ `PdfConverter` class ကို ထပ်ဆောင်း argument များအတွက် ကြည့်ပါ။

```python
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

converter = PdfConverter(
    artifact_dict=create_model_dict(),
)
rendered = converter("FILEPATH")
text, _, images = text_from_rendered(rendered)
```

`rendered` သည် တောင်းဆိုထားသော output အမျိုးအစားပေါ် မူတည်၍ မတူညီသော properties များပါသည့် pydantic basemodel တစ်ခုဖြစ်လိမ့်မည်။ Markdown output (ပုံသေ) ဖြင့် သင့်တွင် `markdown`၊ `metadata` နှင့် `images` properties များ ရှိလိမ့်မည်။ JSON output အတွက်မူ `children`၊ `block_type` နှင့် `metadata` ရှိလိမ့်မည်။

### စိတ်ကြိုက် ဖွဲ့စည်းမှု (Custom configuration)

`ConfigParser` ကို အသုံးပြု၍ configuration ကို ပေးပို့နိုင်သည်။ ရရှိနိုင်သော ရွေးစရာအားလုံးကို ကြည့်ရန် `marker_single --help` ကို လုပ်ပါ။

```python
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.config.parser import ConfigParser

config = {
    "output_format": "json",
    "ADDITIONAL_KEY": "VALUE"
}
config_parser = ConfigParser(config)

converter = PdfConverter(
    config=config_parser.generate_config_dict(),
    artifact_dict=create_model_dict(),
    processor_list=config_parser.get_processors(),
    renderer=config_parser.get_renderer(),
    llm_service=config_parser.get_llm_service()
)
rendered = converter("FILEPATH")
```

### blocks များကို ထုတ်ယူခြင်း (Extract blocks)

စာရွက်စာတမ်းတစ်ခုစီသည် စာမျက်နှာတစ်ခု (သို့) တစ်ခုထက်ပိုသော စာမျက်နှာများ ပါဝင်သည်။ စာမျက်နှာများသည် blocks များ ပါဝင်ပြီး၊ ၎င်းတို့သည် ၎င်းတို့ကိုယ်တိုင် အခြား blocks များ ပါဝင်နိုင်သည်။ ဤ blocks များကို ပရိုဂရမ်အလိုက် ကိုင်တွယ်နိုင်သည်။

ဤသည်မှာ စာရွက်စာတမ်းတစ်ခုမှ ဖောင်များ (forms) အားလုံးကို ထုတ်ယူသည့် ဥပမာ-

```python
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.schema import BlockTypes

converter = PdfConverter(
    artifact_dict=create_model_dict(),
)
document = converter.build_document("FILEPATH")
forms = document.contained_blocks((BlockTypes.Form,))
```

blocks များကို ထုတ်ယူခြင်းနှင့် ကိုင်တွယ်ခြင်းဆိုင်ရာ နမူနာများအတွက် processors များကို ကြည့်ပါ။

## အခြား converter များ (Other converters)

မတူညီသော ပြောင်းလဲခြင်းလုပ်ငန်းစဉ်များကို သတ်မှတ်ပေးသော အခြား converter များကိုလည်း သုံးနိုင်သည်-

### ဇယားများ ထုတ်ယူခြင်း (Extract tables)

`TableConverter` သည် ဇယားများကိုသာ ပြောင်းလဲထုတ်ယူပေးလိမ့်မည်-

```python
from marker.converters.table import TableConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

converter = TableConverter(
    artifact_dict=create_model_dict(),
)
rendered = converter("FILEPATH")
text, _, images = text_from_rendered(rendered)
```

၎င်းသည် PdfConverter နှင့် တူညီသော configuration အားလုံးကို ယူသည်။ layout detection ကို ရှောင်ရှားပြီး စာမျက်နှာတိုင်းကို ဇယားအဖြစ် ယူဆရန် `force_layout_block=Table` configuration ကို သတ်မှတ်နိုင်သည်။ cell bounding boxes များကိုလည်း ရယူရန် `output_format=json` ကို သတ်မှတ်ပါ။

သင်သည် CLI မှတစ်ဆင့် အောက်ပါအတိုင်း run နိုင်သည်-
```shell
marker_single FILENAME --use_llm --force_layout_block Table --converter_cls marker.converters.table.TableConverter --output_format json
```

### OCR သက်သက် (OCR Only)

OCR ကိုသာ run လိုပါက `OCRConverter` မှတစ်ဆင့်လည်း လုပ်ဆောင်နိုင်သည်။ စာလုံးတစ်လုံးချင်းနှင့် bounding boxes များကို ထိန်းသိမ်းရန် `--keep_chars` ကို သတ်မှတ်ပါ။

```python
from marker.converters.ocr import OCRConverter
from marker.models import create_model_dict

converter = OCRConverter(
    artifact_dict=create_model_dict(),
)
rendered = converter("FILEPATH")
```

၎င်းသည် PdfConverter နှင့် တူညီသော configuration အားလုံးကို ယူသည်။

သင်သည် CLI မှတစ်ဆင့် အောက်ပါအတိုင်း run နိုင်သည်-
```shell
marker_single FILENAME --converter_cls marker.converters.ocr.OCRConverter
```

### ဖွဲ့စည်းတည်ဆောက်ပုံဆိုင်ရာ ထုတ်ယူခြင်း (Structured Extraction) (beta)

`ExtractionConverter` မှတစ်ဆင့် structured extraction ကို run နိုင်သည်။ ၎င်းအတွက် llm service တစ်ခု ဦးစွာ setup လုပ်ထားရန် လိုအပ်သည် (အသေးစိတ်အတွက် [ဤနေရာ](#llm-services) ကိုကြည့်ပါ)။ ထုတ်ယူထားသော တန်ဖိုးများပါသော JSON output ကို ရရှိလိမ့်မည်။

```python
from marker.converters.extraction import ExtractionConverter
from marker.models import create_model_dict
from marker.config.parser import ConfigParser
from pydantic import BaseModel

class Links(BaseModel):
    links: list[str]

schema = Links.model_json_schema()
config_parser = ConfigParser({
    "page_schema": schema
})

converter = ExtractionConverter(
    artifact_dict=create_model_dict(),
    config=config_parser.generate_config_dict(),
    llm_service=config_parser.get_llm_service(),
)
rendered = converter("FILEPATH")
```

Rendered တွင် `original_markdown` အကွက်တစ်ခု ပါလိမ့်မည်။ နောက်တစ်ကြိမ် converter ကို run သည့်အခါ ၎င်းကို `existing_markdown` config key အဖြစ် ပြန်လည်ပေးပို့ပါက စာရွက်စာတမ်းကို ပြန်လည် parse လုပ်ခြင်းကို ကျော်နိုင်သည်။

# Output ဖော်မတ်များ (Output Formats)

## Markdown

Markdown output တွင် အောက်ပါတို့ ပါဝင်လိမ့်မည်-

- ရုပ်ပုံလင့်ခ်များ (ရုပ်ပုံများကို တူညီသော ဖိုင်တွဲတွင် သိမ်းဆည်းမည်)
- ပုံစံချထားသော ဇယားများ
- ထည့်သွင်းထားသော LaTeX ညီမျှခြင်းများ (```$$``` ဖြင့် ကာရံထား)
- Code ကို triple backticks ဖြင့် ကာရံထားသည်
- အောက်ခြေမှတ်ချက်များအတွက် Superscripts

## HTML

HTML output သည် markdown output နှင့် ဆင်တူသည်-

- ရုပ်ပုံများကို `img` tags မှတစ်ဆင့် ထည့်သွင်းထားသည်
- ညီမျှခြင်းများကို `<math>` tags ဖြင့် ကာရံထားသည်
- code ကို `pre` tags ထဲတွင် ထည့်သွင်းထားသည်

## JSON

JSON output သည် သစ်ပင်ပုံစံဖွဲ့စည်းမှုဖြင့် စုစည်းထားပြီး အရွက်မ block များမှာ block များဖြစ်သည်။ အရွက်မ block များ၏ ဥပမာများမှာ list item တစ်ခု၊ စာပိုဒ်တစ်ခု (သို့) ရုပ်ပုံတစ်ခု ဖြစ်သည်။

Output သည် စာရင်းတစ်ခုဖြစ်မည်၊ စာရင်းထဲရှိ အရာတစ်ခုစီသည် စာမျက်နှာတစ်ခုကို ကိုယ်စားပြုသည်။ စာမျက်နှာတစ်ခုစီသည် internal marker schema ရှိ block တစ်ခုအဖြစ် သတ်မှတ်ခံရသည်။ မတူညီသော အစိတ်အပိုင်းများကို ကိုယ်စားပြုရန် block အမျိုးအစား အမျိုးမျိုးရှိသည်။

စာမျက်နှာများတွင် သော့များ (keys) ရှိသည်-

- `id` - block အတွက် သီးသန့် ID။
- `block_type` - block အမျိုးအစား။ ဖြစ်နိုင်သော block အမျိုးအစားများကို `marker/schema/__init__.py` တွင် ကြည့်နိုင်သည်။ ဤစာရေးချိန်တွင် ၎င်းတို့မှာ ["Line", "Span", "FigureGroup", "TableGroup", "ListGroup", "PictureGroup", "Page", "Caption", "Code", "Figure", "Footnote", "Form", "Equation", "Handwriting", "TextInlineMath", "ListItem", "PageFooter", "PageHeader", "Picture", "SectionHeader", "Table", "Text", "TableOfContents", "Document"] ဖြစ်သည်။
- `html` - စာမျက်နှာအတွက် HTML ။ သတိပြုရန်- ၎င်းတွင် ကလေး (children) များသို့ recursive references များ ပါလိမ့်မည်။ အကယ်၍ သင်သည် full HTML ကို လိုချင်ပါက `content-ref` tags များကို ကလေး content ဖြင့် အစားထိုးရမည်။ ဥပမာတစ်ခုကို `marker/output.py:json_to_html` တွင် ကြည့်နိုင်သည်။ ၎င်းလုပ်ဆောင်ချက်သည် JSON output မှ block တစ်ခုတည်းကို ယူပြီး HTML အဖြစ်သို့ ပြောင်းလဲပေးလိမ့်မည်။
- `polygon` - စာမျက်နှာ၏ ထောင့် ၄ ခုပါ polygon၊ (x1,y1), (x2,y2), (x3, y3), (x4, y4) ဖော်မတ်ဖြင့်။ (x1,y1) သည် ဘယ်ဘက်အပေါ်ထောင့်ဖြစ်ပြီး သရီးနာရီလက်တံအတိုင်း သွားသည်။
- `children` - ကလေး block များ။

ကလေး block များတွင် နောက်ထပ်သော့နှစ်ခု ထပ်ရှိသည်-

- `section_hierarchy` - block သည် မည်သည့် အပိုင်းများ၏ အစိတ်အပိုင်းဖြစ်သည်ကို ညွှန်ပြသည်။ `1` သည် h1 tag၊ `2` သည် h2 tag စသည်ဖြင့် ဖော်ပြသည်။
- `images` - base64 encoded ရုပ်ပုံများ။ သော့သည် block id ဖြစ်ပြီး data သည် encoded ရုပ်ပုံဖြစ်သည်။

စာမျက်နှာများ၏ ကလေး block များသည် ၎င်းတို့ကိုယ်တိုင် ကိုယ်ပိုင် ကလေးများ ရှိနိုင်သည် (သစ်ပင်ဖွဲ့စည်းပုံ)။

```json
{
      "id": "/page/10/Page/366",
      "block_type": "Page",
      "html": "<content-ref src='/page/10/SectionHeader/0'></content-ref><content-ref src='/page/10/SectionHeader/1'></content-ref><content-ref src='/page/10/Text/2'></content-ref><content-ref src='/page/10/Text/3'></content-ref><content-ref src='/page/10/Figure/4'></content-ref><content-ref src='/page/10/SectionHeader/5'></content-ref><content-ref src='/page/10/SectionHeader/6'></content-ref><content-ref src='/page/10/TextInlineMath/7'></content-ref><content-ref src='/page/10/TextInlineMath/8'></content-ref><content-ref src='/page/10/Table/9'></content-ref><content-ref src='/page/10/SectionHeader/10'></content-ref><content-ref src='/page/10/Text/11'></content-ref>",
      "polygon": [[0.0, 0.0], [612.0, 0.0], [612.0, 792.0], [0.0, 792.0]],
      "children": [
        {
          "id": "/page/10/SectionHeader/0",
          "block_type": "SectionHeader",
          "html": "<h1>Supplementary Material for <i>Subspace Adversarial Training</i> </h1>",
          "polygon": [
            [217.845703125, 80.630859375], [374.73046875, 80.630859375],
            [374.73046875, 107.0],
            [217.845703125, 107.0]
          ],
          "children": null,
          "section_hierarchy": {
            "1": "/page/10/SectionHeader/1"
          },
          "images": {}
        },
        ...
        ]
    }
```

## Chunks (အပိုင်းအစများ)

Chunks ဖော်မတ်သည် JSON နှင့် ဆင်သော်လည်း၊ အရာအားလုံးကို သစ်ပင်အစား စာရင်းပြားတစ်ခုတည်းအဖြစ် ပြောင်းပေးသည်။ စာမျက်နှာတစ်ခုစီမှ ထိပ်ဆုံးအဆင့် block များသာ ပြသသည်။ ၎င်းတွင် block တစ်ခုစီ၏ full HTML ကိုလည်း ထည့်သွင်းထားသောကြောင့် ၎င်းကို ပြန်လည်တည်ဆောက်ရန် သစ်ပင်ကို လှန်ကြည့်စရာမလိုပေ။ ၎င်းသည် RAG အတွက် ပြောင်းလွယ်ပြင်လွယ်နှင့် လွယ်ကူသော chunking ကို ဖွင့်ပေးသည်။

## Metadata (မက်တာဒေတာ)

Output ဖော်မတ်အားလုံးသည် အောက်ပါအကွက်များပါသည့် metadata အဘိဓာန်တစ်ခုကို ပြန်ပေးလိမ့်မည်-

```json
{
    "table_of_contents": [
      {
        "title": "Introduction",
        "heading_level": 1,
        "page_id": 0,
        "polygon": [...]
      }
    ], // computed PDF table of contents
    "page_stats": [
      {
        "page_id":  0,
        "text_extraction_method": "pdftext",
        "block_counts": [("Span", 200), ...]
      },
      ...
    ]
}
```

# LLM ဝန်ဆောင်မှုများ (LLM Services)

`--use_llm` flag ဖြင့် run သည့်အခါ သင်ရွေးချယ်နိုင်သော ဝန်ဆောင်မှုများစွာရှိသည်-

- `Gemini` - ၎င်းသည် မူရင်းအားဖြင့် Gemini developer API ကို သုံးမည်။ သင်သည် `--gemini_api_key` ကို configuration သို့ ပေးရန် လိုအပ်လိမ့်မည်။
- `Google Vertex` - ၎င်းသည် vertex ကို သုံးမည်၊ ၎င်းသည် ပိုမိုစိတ်ချရနိုင်သည်။ သင်သည် `--vertex_project_id` ကို ပေးရန် လိုအပ်လိမ့်မည်။ ၎င်းကို သုံးရန် `--llm_service=marker.services.vertex.GoogleVertexService` ကို သတ်မှတ်ပါ။
- `Ollama` - ၎င်းသည် local models များကို သုံးမည်။ သင်သည် `--ollama_base_url` နှင့် `--ollama_model` ကို configure လုပ်နိုင်သည်။ ၎င်းကို သုံးရန် `--llm_service=marker.services.ollama.OllamaService` ကို သတ်မှတ်ပါ။
- `Claude` - ၎င်းသည် anthropic API ကို သုံးမည်။ သင်သည် `--claude_api_key` နှင့် `--claude_model_name` ကို configure လုပ်နိုင်သည်။ ၎င်းကို သုံးရန် `--llm_service=marker.services.claude.ClaudeService` ကို သတ်မှတ်ပါ။
- `OpenAI` - ၎င်းသည် openai-like endpoint များကို ထောက်ပံ့သည်။ သင်သည် `--openai_api_key`၊ `--openai_model` နှင့် `--openai_base_url` ကို configure လုပ်နိုင်သည်။ ၎င်းကို သုံးရန် `--llm_service=marker.services.openai.OpenAIService` ကို သတ်မှတ်ပါ။
- `Azure OpenAI` - ၎င်းသည် Azure OpenAI ဝန်ဆောင်မှုကို သုံးမည်။ သင်သည် `--azure_endpoint`၊ `--azure_api_key` နှင့် `--deployment_name` ကို configure လုပ်နိုင်သည်။ ၎င်းကို သုံးရန် `--llm_service=marker.services.azure_openai.AzureOpenAIService` ကို သတ်မှတ်ပါ။

ဤဝန်ဆောင်မှုများတွင် နောက်ထပ် optional configuration များ ရှိနိုင်သည် - သင်သည် class များကို ကြည့်ရှုခြင်းဖြင့် ၎င်းတို့ကို မြင်နိုင်သည်။

# အတွင်းပိုင်း (Internals)

Marker သည် တိုးချဲ့ရန် လွယ်ကူသည်။ marker ၏ အဓိက ယူနစ်များမှာ-

- `Providers`, `marker/providers` တွင်။ ဤအရာများသည် source file တစ်ခုမှ အချက်အလက်များကို ပံ့ပိုးပေးသည်၊ ဥပမာ PDF ။
- `Builders`, `marker/builders` တွင်။ ဤအရာများသည် ကနဦး စာရွက်စာတမ်း block များကို ထုတ်ပေးပြီး providers များမှ အချက်အလက်များကို အသုံးပြု၍ စာသားများ ဖြည့်သွင်းသည်။
- `Processors`, `marker/processors` တွင်။ ဤအရာများသည် တိကျသော block များကို လုပ်ဆောင်သည်၊ ဥပမာ table formatter သည် processor တစ်ခုဖြစ်သည်။
- `Renderers`, `marker/renderers` တွင်။ ဤအရာများသည် output ကို render လုပ်ရန် block များကို အသုံးပြုသည်။
- `Schema`, `marker/schema` တွင်။ block အမျိုးအစားအားလုံးအတွက် class များ။
- `Converters`, `marker/converters` တွင်။ ၎င်းတို့သည် end to end pipeline တစ်ခုလုံးကို run သည်။

processing အပြုအမူကို စိတ်ကြိုက်ပြုလုပ်ရန် `processors` ကို override လုပ်ပါ။ output ဖော်မတ်အသစ်များ ထည့်ရန် `renderer` အသစ်တစ်ခု ရေးပါ။ ထပ်ဆောင်း input ဖော်မတ်များအတွက် `provider` အသစ်တစ်ခု ရေးပါ။

Processors နှင့် renderers များကို base `PDFConverter` သို့ တိုက်ရိုက် ပေးပို့နိုင်သောကြောင့် သင်သည် သင့်ကိုယ်ပိုင် custom processing ကို အလွယ်တကူ သတ်မှတ်နိုင်သည်။

## API server

အောက်ပါအတိုင်း run နိုင်သော အလွန်ရိုးရှင်းသော API server တစ်ခုရှိသည်-

```shell
pip install -U uvicorn fastapi python-multipart
marker_server --port 8001
```

၎င်းသည် fastapi server တစ်ခုကို စတင်မည်၊ သင်သည် `localhost:8001` တွင် ဝင်ရောက်နိုင်သည်။ endpoint options များကို ကြည့်ရန် `localhost:8001/docs` သို့ သွားနိုင်သည်။

သင်သည် ဤကဲ့သို့ request များ ပေးပို့နိုင်သည်-

```
import requests
import json

post_data = {
    'filepath': 'FILEPATH',
    # Add other params here
}

requests.post("http://localhost:8001/marker", data=json.dumps(post_data)).json()
```

ဤသည်မှာ အလွန်ခိုင်မာသော API မဟုတ်ကြောင်း သတိပြုပါ၊ ၎င်းသည် အသေးစားအသုံးပြုရန်အတွက်သာ ရည်ရွယ်သည်။ အကယ်၍ သင်သည် ဤ server ကို သုံးလိုသော်လည်း ပိုမိုခိုင်မာသော conversion option ကို လိုချင်ပါက၊ hosted [Datalab API](https://www.datalab.to/plans) ကို သုံးနိုင်သည်။

# ပြဿနာဖြေရှင်းခြင်း (Troubleshooting)

သင်မျှော်လင့်ထားသည့်အတိုင်း အရာများ အလုပ်မလုပ်ပါက အသုံးဝင်နိုင်သော ဆက်တင်အချို့-

- တိကျမှုပြဿနာများရှိပါက `--use_llm` ကို သတ်မှတ်၍ LLM ကို အရည်အသွေးမြှင့်တင်ရန် ကြိုးစားပါ။ ၎င်းအလုပ်လုပ်ရန် သင်သည် `GOOGLE_API_KEY` ကို Gemini API key တစ်ခုသို့ သတ်မှတ်ရမည်။
- စာသားများ ပျက်စီးနေသည်ကို တွေ့ပါက `force_ocr` ကို သတ်မှတ်ပါ - ၎င်းသည် စာရွက်စာတမ်းကို ပြန်လည် OCR လုပ်ပေးမည်။
- `TORCH_DEVICE` - ၎င်းကို inference အတွက် ပေးထားသော torch device ကို အသုံးပြုရန် marker ကို အတင်းအကြပ်လုပ်ရန် သတ်မှတ်ပါ။
- memory လွန်ကဲမှု အမှားများ ကြုံနေရပါက လုပ်သားအရေအတွက်ကို လျှော့ချပါ။ ရှည်လျားသော PDF များကို ဖိုင်များစွာခွဲခြင်းကိုလည်း ကြိုးစားနိုင်သည်။

## Debugging (အမှားရှာခြင်း)

debug mode ကို ဖွင့်ရန် `debug` option ကို ပေးပါ။ ၎င်းသည် စာမျက်နှာတစ်ခုစီ၏ ရှာဖွေတွေ့ရှိထားသော layout နှင့် စာသားပါသည့် ရုပ်ပုံများကို သိမ်းဆည်းပေးမည်၊ ထို့အပြင် နောက်ထပ် bounding box အချက်အလက်များပါသည့် JSON ဖိုင်ကိုလည်း output ထုတ်ပေးမည်။

# စံညွှန်းများ (Benchmarks)

## အလုံးစုံ PDF ပြောင်းလဲခြင်း (Overall PDF Conversion)

ကျွန်ုပ်တို့သည် common crawl မှ PDF စာမျက်နှာတစ်ခုချင်းစီကို ထုတ်ယူခြင်းဖြင့် [စံညွှန်းအစု](https://huggingface.co/datasets/datalab-to/marker_benchmark) တစ်ခုကို ဖန်တီးခဲ့သည်။ ကျွန်ုပ်တို့သည် ground truth စာသားအပိုင်းအစများနှင့် ကိုက်ညီသော heuristic တစ်ခု၊ နှင့် LLM အကဲဖြတ် ရမှတ်သတ်မှတ်ခြင်းနည်းလမ်းတစ်ခုအပေါ် အခြေခံ၍ အမှတ်ပေးခဲ့သည်။

| Method     | Avg Time | Heuristic Score | LLM Score |
|------------|----------|-----------------|-----------|
| marker     | 2.83837  | 95.6709         | 4.23916   |
| llamaparse | 23.348   | 84.2442         | 3.97619   |
| mathpix    | 6.36223  | 86.4281         | 4.15626   |
| docling    | 3.69949  | 86.7073         | 3.70429   |

စံညွှန်းများကို marker နှင့် docling အတွက် H100 တွင် run ခဲ့သည် - llamaparse နှင့် mathpix သည် ၎င်းတို့၏ cloud ဝန်ဆောင်မှုများကို အသုံးပြုခဲ့သည်။ စာရွက်စာတမ်းအမျိုးအစားအလိုက်လည်း ကြည့်နိုင်သည်-

<img src="data/images/per_doc.png" width="1000px"/>

| Document Type        | Marker heuristic | Marker LLM | Llamaparse Heuristic | Llamaparse LLM | Mathpix Heuristic | Mathpix LLM | Docling Heuristic | Docling LLM |
|----------------------|------------------|------------|----------------------|----------------|-------------------|-------------|-------------------|-------------|
| Scientific paper     | 96.6737          | 4.34899    | 87.1651              | 3.96421        | 91.2267           | 4.46861     | 92.135            | 3.72422     |
| Book page            | 97.1846          | 4.16168    | 90.9532              | 4.07186        | 93.8886           | 4.35329     | 90.0556           | 3.64671     |
| Other                | 95.1632          | 4.25076    | 81.1385              | 4.01835        | 79.6231           | 4.00306     | 83.8223           | 3.76147     |
| Form                 | 88.0147          | 3.84663    | 66.3081              | 3.68712        | 64.7512           | 3.33129     | 68.3857           | 3.40491     |
| Presentation         | 95.1562          | 4.13669    | 81.2261              | 4              | 83.6737           | 3.95683     | 84.8405           | 3.86331     |
| Financial document   | 95.3697          | 4.39106    | 82.5812              | 4.16111        | 81.3115           | 4.05556     | 86.3882           | 3.8         |
| Letter               | 98.4021          | 4.5        | 93.4477              | 4.28125        | 96.0383           | 4.45312     | 92.0952           | 4.09375     |
| Engineering document | 93.9244          | 4.04412    | 77.4854              | 3.72059        | 80.3319           | 3.88235     | 79.6807           | 3.42647     |
| Legal document       | 96.689           | 4.27759    | 86.9769              | 3.87584        | 91.601            | 4.20805     | 87.8383           | 3.65552     |
| Newspaper page       | 98.8733          | 4.25806    | 84.7492              | 3.90323        | 96.9963           | 4.45161     | 92.6496           | 3.51613     |
| Magazine page        | 98.2145          | 4.38776    | 87.2902              | 3.97959        | 93.5934           | 4.16327     | 93.0892           | 4.02041     |

## Throughput (ထွက်ရှိနှုန်း)

ကျွန်ုပ်တို့သည် [ရှည်လျားသော PDF တစ်ခုတည်း](https://www.greenteapress.com/thinkpython/thinkpython.pdf) ကို အသုံးပြု၍ throughput ကို စံညွှန်းသတ်မှတ်ခဲ့သည်။

| Method  | Time per page | Time per document | VRAM used |
|---------|---------------|-------------------|---------- |
| marker  | 0.18          | 43.42             |  3.17GB   |

ခန့်မှန်းခြေ throughput သည် H100 တွင် တစ်စက္ကန့်လျှင် စာမျက်နှာ ၁၂၂ မျက်နှာ - ပေးထားသော VRAM အသုံးပြုမှုဖြင့် ကျွန်ုပ်တို့သည် လုပ်ငန်းစဉ် ၂၂ ခုကို တစ်ပြိုင်နက် run နိုင်သည်။

## ဇယားပြောင်းလဲခြင်း (Table Conversion)

Marker သည် `marker.converters.table.TableConverter` ကို အသုံးပြု၍ PDF များမှ ဇယားများကို ထုတ်ယူနိုင်သည်။ ဇယားထုတ်ယူမှု စွမ်းဆောင်ရည်ကို [FinTabNet](https://developer.ibm.com/exchanges/data/all/fintabnet/) ၏ test split ကို အသုံးပြု၍ ထုတ်ယူထားသော ဇယားများ၏ HTML ကိုယ်စားပြုမှုကို မူရင်း HTML ကိုယ်စားပြုမှုများနှင့် နှိုင်းယှဉ်ခြင်းဖြင့် တိုင်းတာသည်။ HTML ကိုယ်စားပြုမှုများကို ဖွဲ့စည်းပုံနှင့် အကြောင်းအရာ နှစ်မျိုးလုံးကို အကဲဖြတ်ရန် tree edit distance အခြေခံ မက်ထရစ်ကို အသုံးပြု၍ နှိုင်းယှဉ်သည်။ Marker သည် PDF စာမျက်နှာတစ်ခုရှိ ဇယားအားလုံး၏ ဖွဲ့စည်းပုံကို ရှာဖွေဖော်ထုတ်ပြီး အောက်ပါရမှတ်များ ရရှိသည်-

| Method           | Avg score | Total tables |
|------------------|-----------|--------------|
| marker           | 0.816     | 99           |
| marker w/use_llm | 0.907     | 99           |
| gemini           | 0.829     | 99           |

`--use_llm` flag သည် ဇယားမှတ်မိခြင်း စွမ်းဆောင်ရည်ကို သိသိသာသာ မြှင့်တင်နိုင်သည်၊ သင်မြင်ရသည့်အတိုင်းဖြစ်သည်။

ကျွန်ုပ်တို့၏ layout model နှင့် fintabnet သည် detection နည်းလမ်းများ အနည်းငယ်ကွဲပြားသောကြောင့် ground truth နှင့် မကိုက်ညီနိုင်သော ဇယားများကို စစ်ထုတ်ပါသည် (ဤသို့ဖြင့် အချို့ဇယားများကို ခွဲခြင်း/ပေါင်းစည်းခြင်း ဖြစ်နေသည်)။

## သင့်ကိုယ်ပိုင် စံညွှန်းများ (benchmarks) ကို run ခြင်း

သင်သည် သင့်စက်ပေါ်တွင် marker ၏ စွမ်းဆောင်ရည်ကို စံညွှန်းသတ်မှတ်နိုင်သည်။ marker ကို အောက်ပါအတိုင်း ကိုယ်တိုင်တပ်ဆင်ပါ-

```shell
git clone https://github.com/VikParuchuri/marker.git
poetry install
```

### အလုံးစုံ PDF ပြောင်းလဲခြင်း (Overall PDF Conversion)

စံညွှန်းဒေတာကို [ဤနေရာ](https://drive.google.com/file/d/1ZSeWDo2g1y0BRLT7KnbmytV2bjWARWba/view?usp=sharing) တွင် ဒေါင်းလုဒ်လုပ်ပြီး ဇစ်ဖြေပါ။ ထို့နောက် အလုံးစုံစံညွှန်းကို အောက်ပါအတိုင်း run ပါ-

```shell
python benchmarks/overall.py --methods marker --scores heuristic,llm
```

ရွေးစရာများ (Options):

- `--use_llm` marker ရလဒ်များကို မြှင့်တင်ရန် llm ကို သုံးပါ။
- `--max_rows` စံညွှန်းအတွက် မည်မျှအတန်းအထိ လုပ်ဆောင်ရမည်။
- `--methods` `llamaparse`, `mathpix`, `docling`, `marker` ဖြစ်နိုင်သည်။ Comma ခြားပါ။
- `--scores` မည်သည့် scoring functions ကို သုံးမည်၊ `llm`, `heuristic` ဖြစ်နိုင်သည်။ Comma ခြားပါ။

### ဇယားပြောင်းလဲခြင်း (Table Conversion)
လုပ်ဆောင်ပြီးသား FinTabNet dataset ကို [ဤနေရာ](https://huggingface.co/datasets/datalab-to/fintabnet-test) တွင် hosting လုပ်ထားပြီး အလိုအလျောက် ဒေါင်းလုဒ်လုပ်သည်။ စံညွှန်းကို အောက်ပါအတိုင်း run ပါ-

```shell
python benchmarks/table/table.py --max_rows 100
```

ရွေးစရာများ (Options):

- `--use_llm` တိကျမှုတိုးတက်စေရန် marker နှင့်အတူ llm ကို သုံးပါ။
- `--use_gemini` gemini 2.0 flash ကိုလည်း စံညွှန်းသတ်မှတ်ပါ။

# ၎င်းမည်သို့အလုပ်လုပ်ပုံ (How it works)

Marker သည် deep learning မော်ဒယ်များ၏ pipeline တစ်ခုဖြစ်သည်-

- စာသားထုတ်ယူခြင်း၊ လိုအပ်ပါက OCR (heuristics, [surya](https://github.com/VikParuchuri/surya))
- စာမျက်နှာ layout ကို ရှာဖွေပြီး ဖတ်ရှုမှုအစဉ် (reading order) ကို သိရှိခြင်း ([surya](https://github.com/VikParuchuri/surya))
- block တစ်ခုစီကို သန့်ရှင်းရေးလုပ်ပြီး ပုံစံချခြင်း (heuristics, [texify](https://github.com/VikParuchuri/texify), [surya](https://github.com/VikParuchuri/surya))
- အရည်အသွေးမြှင့်တင်ရန် စိတ်ကြိုက် LLM ကို အသုံးပြုခြင်း
- blocks များကို ပေါင်းစည်းပြီး စာသားအပြည့်အစုံကို postprocess လုပ်ခြင်း

၎င်းသည် လိုအပ်သည့်နေရာတွင်သာ မော်ဒယ်များကို အသုံးပြုသောကြောင့် အမြန်နှုန်းနှင့် တိကျမှုကို ပိုမိုကောင်းမွန်စေသည်။

# ကန့်သတ်ချက်များ (Limitations)

PDF သည် ခက်ခဲသော ဖော်မတ်တစ်ခုဖြစ်သောကြောင့် marker သည် အမြဲတမ်း အပြည့်အဝ အလုပ်မလုပ်နိုင်ပါ။ ဖြေရှင်းရန် လမ်းပြမြေပုံပေါ်တွင် ရှိသော သိထားသည့် ကန့်သတ်ချက်အချို့-

- အလွန်ရှုပ်ထွေးသော layouts၊ nested tables နှင့် forms များပါသော စာရွက်စာတမ်းများ အလုပ်မလုပ်နိုင်ပါ။
- ဖောင်များ (forms) ကောင်းစွာ မထွက်ရှိနိုင်ပါ။

မှတ်ချက်- `--use_llm` နှင့် `--force_ocr` flags များကို ပေးပါက ဤပြဿနာအများစုကို ဖြေရှင်းပေးလိမ့်မည်။

# အသုံးပြုမှုနှင့် အသုံးချမှု နမူနာများ (Usage and Deployment Examples)

သင်သည် `marker` ကို အမြဲ local တွင် run နိုင်သော်လည်း ၎င်းကို API အဖြစ် ဖော်ထုတ်လိုပါက ရွေးစရာအချို့ရှိသည်-
- ကျွန်ုပ်တို့၏ platform API သည် `marker` နှင့် `surya` ဖြင့် မောင်းနှင်ထားပြီး စမ်းသပ်ရန် လွယ်ကူသည် - ၎င်းကို အခမဲ့ စာရင်းသွင်းနိုင်ပြီး ကျွန်ုပ်တို့သည် credits များ ထည့်ပေးမည်၊ [ဤနေရာတွင် စမ်းကြည့်ပါ](https://datalab.to)
- စီးပွားဖြစ်အသုံးပြုမှုအတွက် ကျွန်ုပ်တို့၏ ပူပန်စရာမလိုသော on-prem solution၊ ၎င်းအကြောင်းကို [ဤနေရာတွင် ဖတ်ရှုနိုင်ပါသည်](https://www.datalab.to/blog/self-serve-on-prem-licensing) ၎င်းသည် သင့်အား လျှို့ဝှက်ရေးအာမခံချက်များနှင့်အတူ မြင့်မားသော throughput inference optimization များကို ပေးသည်။
- [Modal ဖြင့် deployment နမူနာ](./examples/README_MODAL.md) သည် [`Modal`](https://modal.com) ကို အသုံးပြု၍ marker ကို web endpoint တစ်ခုမှတစ်ဆင့် မည်သို့ deploy လုပ်ပြီး ဝင်ရောက်အသုံးပြုနိုင်သည်ကို ပြသထားသည်။ Modal သည် AI compute platform တစ်ခုဖြစ်ပြီး developer များအား မိနစ်ပိုင်းအတွင်း GPUs ပေါ်တွင် မော်ဒယ်များ deploy လုပ်ကာ scale လုပ်နိုင်စေပါသည်။
```
