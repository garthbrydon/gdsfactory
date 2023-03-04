from sqlalchemy import Column, JSON
from sqlalchemy.orm import Mapped, mapped_column

from gdsfactory.database.base_class import Base


class SParameterResult(Base):
    __table_args__ = {"comment": "This table holds scattering parameter results."}

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    n_ports: Mapped[int] = mapped_column(nullable=False)
    # unmapped array col, needs special JSON serialization
    array = Column(JSON, nullable=False)
