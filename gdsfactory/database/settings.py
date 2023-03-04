import logging
import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

DB_CONNECTION_STRING = os.environ.get("DB_CONNECTION_STRING", "[SETME]")
LOG_LEVEL = os.environ.get("LOG_LEVEL", logging.INFO)
DB_USE_PSQL = os.environ.get("DB_USE_PSQL", True)
