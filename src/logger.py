"""
This module configures logging for the application using settings from the configuration module.
The logger writes logs to a file specified in the configuration.
"""

import logging
from src import config

logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=config.LOG_FILE,
    filemode='a'
)
logger = logging.getLogger(__name__)
