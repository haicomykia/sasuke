from sqlalchemy import Column, Integer, Unicode
from sqlalchemy import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp

from core.database import ModelBase
from models.base import Base


class Balances(ModelBase, Base):
    """
    差引残高テーブル
    """
    __tablename__ = 't_balances'
    __table_args__ = {
        'comment': '差引残高テーブル'
    }

    balance_id = Column(Integer, primary_key=True, autoincrement=True, comment="差引残高ID")
    customer_id = Column(Integer, nullable=True, comment="顧客ID")
    bank_id = Column(Integer, nullable=True, comment="銀行ID")
    created_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="作成日")
    updated_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="更新日")
    deleted_at = Column(Timestamp, nullable=True, comment="削除日")
