import logging
import os
from pathlib import Path
from rustore_downloader.config.settings import settings

def setup_logger():
    """Configure application logging"""
    settings.ensure_directories_exist()
    log_file = os.path.join(settings.LOG_DIR, settings.LOG_FILE)
    
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

logger = setup_logger()