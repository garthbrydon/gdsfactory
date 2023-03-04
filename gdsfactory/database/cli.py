import logging

from fire import Fire

from gdsfactory.database.commands import DatabaseCommands
from gdsfactory.database.settings import LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL)


def fire_db_cli():
    """Run Database Commands object via typical cli."""
    Fire(DatabaseCommands)
