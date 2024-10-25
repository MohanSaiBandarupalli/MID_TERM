"""
This module loads environment variables and sets default configurations for the application.
It uses the `dotenv` library to load variables from a `.env` 
file and provides default values if not present.
"""

import os
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()
# Define configuration variables with defaults
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
HISTORY_FILE = os.getenv("HISTORY_FILE", "./data/history.csv")
LOG_FILE = os.getenv("LOG_FILE", "./logs/log.log")
