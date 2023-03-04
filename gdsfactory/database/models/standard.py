from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from gdsfactory.database.base_class import Base


class Process(Base):
    __table_args__ = {"comment": "This table holds all foundry process info."}

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    process: Mapped[str]
    version: Mapped[str]
    type: Mapped[str]
    description: Mapped[str]


class Unit(Base):
    __table_args__ = {
        "comment": "This table holds all units. A unit is here understood as definite magnitude of a quantity."
    }

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    quantity: Mapped[str]
    symbol: Mapped[str]
    description: Mapped[str]
    unit_results: Mapped[List["Result"]] = relationship(back_populates="unit")
    domain_unit_results: Mapped[List["Result"]] = relationship(
        back_populates="domain_unit"
    )
    unit_computed_results: Mapped[List["ComputedResult"]] = relationship(
        back_populates="unit"
    )
    domain_unit_computed_results: Mapped[List["ComputedResult"]] = relationship(
        back_populates="domain_unit"
    )


class Wafer(Base):
    __table_args__ = {"comment": "This table holds the base definition of a wafer."}

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    serial_number: Mapped[str]
    description: Mapped[str]
    reticles: Mapped[List["Reticle"]] = relationship(back_populates="wafer")


class Reticle(Base):
    __table_args__ = {"comment": "This table holds the definition of a reticle."}

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    description: Mapped[str]
    position: Mapped[str] = mapped_column(
        comment="Position of the reticle on the wafer. (ROW, COLUMN)"
    )
    size: Mapped[str] = mapped_column(
        comment="The size of the reticle (X,Y) having the convention that -Å· points towards the notch/flat of the wafer.",
    )
    wafer_id: Mapped[int] = mapped_column(
        ForeignKey("wafer.id"), nullable=False, index=True
    )
    wafer: Mapped["Wafer"] = relationship(back_populates="reticles")


class ComputedResult(Base):
    __table_args__ = {
        "comment": "This table holds all results obtained after computation/analysis of the raw results contained in the table result."
    }

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    type: Mapped[str]
    description: Mapped[str]
    value: Mapped[str] = mapped_column(Text, deferred=True)
    domain: Mapped[str] = mapped_column(Text, deferred=True)

    unit_id: Mapped[int] = mapped_column(ForeignKey("unit.id"), index=True)
    unit: Mapped["Unit"] = relationship(
        primaryjoin="ComputedResult.unit_id == Unit.id",
        back_populates="unit_computed_results",
    )

    domain_unit_id: Mapped[int] = mapped_column(ForeignKey("unit.id"), index=True)
    domain_unit: Mapped["Unit"] = relationship(
        primaryjoin="ComputedResult.domain_unit_id == Unit.id",
        back_populates="domain_unit_computed_results",
    )


class Result(Base):
    __table_args__ = {"comment": "This table holds all results."}

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    type: Mapped[str]
    description: Mapped[str]
    value: Mapped[str] = mapped_column(Text, deferred=True)
    domain: Mapped[str] = mapped_column(Text, deferred=True)

    unit_id: Mapped[int] = mapped_column(ForeignKey("unit.id"), index=True)
    unit: Mapped["Unit"] = relationship(
        primaryjoin="Result.unit_id == Unit.id", back_populates="unit_results"
    )

    domain_unit_id: Mapped[int] = mapped_column(ForeignKey("unit.id"), index=True)
    domain_unit: Mapped["Unit"] = relationship(
        primaryjoin="Result.domain_unit_id == Unit.id",
        back_populates="domain_unit_results",
    )
