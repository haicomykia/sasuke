from sqlalchemy import Column, Integer, Unicode, String, DateTime
from sqlalchemy import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp

from core.database import ModelBase
from models.base import Base

class SousaTypes(ModelBase, Base):
    """
    操作ログテーブル
    """
    __tablename__ = 'm_sousa_types'
    __table_args__ = {
        'comment': '操作区分マスタ'
    }

    sousa_id = Column(Integer, primary_key=True, comment="操作区分ID")
    sousa_name = Column(String, nullable=False, comment="操作区分名")