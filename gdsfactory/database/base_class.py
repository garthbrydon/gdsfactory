from datetime import datetime
from typing import Any, Dict

from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr

class_registry: Dict = {}


@as_declarative(class_registry=class_registry)
class Base:
    id: Any
    __name__: str
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
