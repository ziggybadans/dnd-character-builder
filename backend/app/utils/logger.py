import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from ..config import get_settings

settings = get_settings()

# Create logs directory if it doesn't exist
log_dir = settings.BASE_DIR / "logs"
log_dir.mkdir(exist_ok=True)


# Configure logging
def setup_logger(name: str) -> logging.Logger:
    """Set up and return a logger instance with both file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create formatters
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_formatter = logging.Formatter("%(levelname)s: %(message)s")

    # File handler (rotating log files)
    file_handler = RotatingFileHandler(
        log_dir / "app.log", maxBytes=10485760, backupCount=5  # 10MB
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(file_formatter)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Create main application logger
logger = setup_logger("dnd_character_builder")
