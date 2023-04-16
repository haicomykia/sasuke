from typing import Optional
import os
import yaml
from logging import config, getLogger, Logger

from pathlib import Path

def get_config_yaml_dir() -> str:
    BASE_URL = str(Path(__file__).parent.parent.parent.absolute())
    return os.path.join(BASE_URL, 'logger_config.yaml')

def init_logger() -> Optional[str]:
    try:
        with open(get_config_yaml_dir(), 'r') as f:
            setting = yaml.safe_load(f)
            config.dictConfig(setting)
    except Exception as e:
        return str(e)

def get_logger(name: str) -> Logger:
    return getLogger(name)