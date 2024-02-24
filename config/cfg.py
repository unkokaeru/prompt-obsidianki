"""Configuration file"""

import os
from pathlib import Path

from dotenv import load_dotenv
from rich.logging import RichHandler

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(message)s",
    "datefmt": "[%X]",
    "handlers": [RichHandler(rich_tracebacks=True)],
}

# OpenAI API Configuration
load_dotenv(dotenv_path=Path(__file__).parent / ".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = "asst_srYMhf0V7Rstyegnaqak6MLG"

# Save location
SAVE_LOCATION = Path(__file__).parent.parent / "notes"
