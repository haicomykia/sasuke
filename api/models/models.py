from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Unicode
from sqlalchemy import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp

ModelBase = declarative_base()

"""
SQL Alchemyのモデル
"""

class AccountTitle(ModelBase):
    """
    勘定科目マスタ
    """
    __tablename__ = 'm_account_titles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title_name = Column(Unicode(100))
    title_group_code = Column(Integer, nullable=False)
    version_id = Column(Integer, default=1)
    created_at = Column(Timestamp, default=current_timestamp())
    updated_at = Column(Timestamp, default=current_timestamp())
    deleted_at = Column(Timestamp, default=current_timestamp())