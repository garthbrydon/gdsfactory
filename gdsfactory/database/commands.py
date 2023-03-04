import logging
from typing import List

from fastapi.encoders import jsonable_encoder

from gdsfactory.database.schemas.standard import Wafer


class DatabaseCommands(object):
    """
    Available Database commands
    """

    def __init__(self):
        """
        Initialize object with commands related to Database functionality
        """
        self.__log = logging.info
        self.__err = logging.error

        from gdsfactory.database.session import SessionLocal
        from gdsfactory.database.services.standard import wafer_service

        self.db = SessionLocal()
        self.wafer_svc = wafer_service

    def __get_db(self):
        try:
            yield self.db
        finally:
            self.db.close()

    def add_wafer(
        self,
        name: str,
    ):
        """Adds a wafer to the db
        Parameters
        ----------
        name : string
          Name to identify wafer
        reticles : list?
        """
        wafer = self.wafer_svc.create_with_reticles(
            next(self.__get_db()), name, "asdsadasd", []
        )
        self.__log(f"Created new wafer. Id: {wafer.id}")
