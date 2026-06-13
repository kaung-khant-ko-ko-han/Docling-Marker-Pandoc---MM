project/
├── main.py                 # CLI entry point
├── config.py               # Configuration loader
├── converter.py            # Marker integration and conversion logic
├── chapter_splitter.py     # Chapter detection and splitting
├── chunker.py              # LLM translation chunk preparation
├── validator.py            # Quality validation
├── metadata.py             # Metadata extraction
├── models.py               # Pydantic models
├── utils.py                # Helpers, logging, checkpointing
├── config.yaml             # Default configuration
├── requirements.txt        # Dependencies
├── README.md               # Documentation
└── tests/                  # Unit tests
    ├── test_converter.py
    ├── test_chapter_splitter.py
    ├── test_chunker.py
    └── test_validator.py
