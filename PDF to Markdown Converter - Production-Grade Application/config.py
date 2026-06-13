"""Load and validate YAML configuration."""

import yaml
import logging
from pathlib import Path
from typing import Optional
from .models import AppConfig

logger = logging.getLogger(__name__)


def load_config(config_path: Optional[Path] = None) -> AppConfig:
    """Load configuration from YAML file or defaults."""
    if config_path is None:
        config_path = Path("config.yaml")
    
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if data is None:
                data = {}
            return AppConfig(**data)
        except yaml.YAMLError as e:
            logger.warning(f"YAML parse error in {config_path}: {e}. Using defaults.")
            return AppConfig()
        except (FileNotFoundError, IOError) as e:
            logger.warning(f"Failed to read {config_path}: {e}. Using defaults.")
            return AppConfig()
        except ValueError as e:
            logger.warning(f"Invalid config values: {e}. Using defaults.")
            return AppConfig()
    else:
        logger.info(f"Config file {config_path} not found. Using defaults.")
        return AppConfig()
