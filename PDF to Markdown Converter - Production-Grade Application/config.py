"""Load and validate YAML configuration."""

import yaml
from pathlib import Path
from typing import Optional
from .models import AppConfig


def load_config(config_path: Optional[Path] = None) -> AppConfig:
    """Load configuration from YAML file or defaults."""
    if config_path is None:
        config_path = Path("config.yaml")
    
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return AppConfig(**data)
    else:
        return AppConfig()
