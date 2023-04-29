from sqlalchemy import Column, String
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase

from core.database import ModelBase
from models.base import Base


class User(SQLAlchemyBaseUserTableUUID, ModelBase):
    user_name = Column(String, nullable=False, comment="ユーザー名")