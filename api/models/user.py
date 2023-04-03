from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.orm import DeclarativeMeta, declarative_base

from models.base import Base


ModelBase: DeclarativeMeta = declarative_base()

class User(SQLAlchemyBaseUserTableUUID, ModelBase, Base):
    pass