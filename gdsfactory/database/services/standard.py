from typing import Any, Dict, List, Optional, Union

from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from gdsfactory.database.models.standard import Wafer, Reticle
from gdsfactory.database.schemas.standard import WaferCreate, WaferUpdate, ReticleCreate
from gdsfactory.database.services.base import ServiceBase


class WaferService(ServiceBase[Wafer, WaferCreate, WaferUpdate]):
    """Wafer service"""

    def get_by_reticle_name(self, db: Session, *, reticle_name: str) -> Optional[Wafer]:
        """Get Wafer by reticle name
        Parameters
        ----------
        reticle_name : string
        """
        return (
            db.query(Wafer)
            .join(Reticle)
            .filter(func.lower(Reticle.name) == func.lower(reticle_name))
            .first()
        )

    def update(
        self, db: Session, *, db_obj: Wafer, obj_in: Union[WaferUpdate, Dict[str, Any]]
    ) -> Wafer:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def create_with_reticles(
        self, db: Session, name: str, serial_number: str, reticles: List[ReticleCreate]
    ) -> Wafer:
        """Adds a wafer and its reticles to the db
        Parameters
        ----------
        name : string
          Name to identify wafer
        reticles : list
          List of reticles to add to this wafer
        """
        wafer = Wafer(name=name, serial_number=serial_number)  # type: ignore

        for reticle_input in reticles:
            reticle = Reticle(
                name=reticle_input.name,
                description=reticle_input.description,
                position=reticle_input.position,
                size=reticle_input.size,
            )
            wafer.reticles.append(reticle)

        db.add(wafer)
        db.commit()
        db.refresh(wafer)
        return wafer


wafer_service = WaferService(Wafer)
