import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from gdsfactory.database.settings import DB_CONNECTION_STRING, DB_USE_PSQL

from gdsfactory.database.serialization import (
    GdsfactoryJSONEncoder,
    GdsfactoryJSONDecoder,
)


if DB_USE_PSQL is True:
    engine = create_engine(
        DB_CONNECTION_STRING,
        pool_size=5,
        max_overflow=2,
        pool_timeout=30,  # 30 seconds
        pool_recycle=1800,  # 30 minutes
        json_serializer=partial(json.dumps, cls=GdsfactoryJSONEncoder),
        json_deserializer=partial(json.loads, cls=GdsfactoryJSONDecoder),
    )
else:
    engine = create_engine(
        DB_CONNECTION_STRING,
        # required for sqlite
        connect_args={"check_same_thread": False},
        json_serializer=partial(json.dumps, cls=GdsfactoryJSONEncoder),
        json_deserializer=partial(json.loads, cls=GdsfactoryJSONDecoder),
    )


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
