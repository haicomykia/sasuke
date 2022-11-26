from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Unicode, ForeignKey
from sqlalchemy import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp

ModelBase = declarative_base()

"""
SQL Alchemyのモデル
"""


class AccountTitleGroups(ModelBase):
    """
    勘定科目グループマスタ
    """
    __tablename__ = 'm_kanjo_kamoku_group'
    __table_args__ = {
        'comment': '勘定科目グループマスタ'
    }

    kanjo_kamoku_group_code = Column(Integer, primary_key=True, autoincrement=True, comment="勘定科目グループコード")
    group_name = Column(Unicode(100), comment="勘定科目名")
    version_id = Column(Integer, default=1, nullable=False, comment="バージョンID")
    created_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="作成日")
    updated_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="更新日")
    deleted_at = Column(Timestamp, default=current_timestamp(), comment="削除日")


class AccountTitle(ModelBase):
    """
    勘定科目マスタ
    """
    __tablename__ = 'm_kanjo_kamoku'
    __table_args__ = {
        'comment': '勘定科目マスタ'
    }

    kanjo_kamoku_id = Column(Integer, primary_key=True, autoincrement=True, comment="勘定科目ID")
    kanjo_kamoku_name = Column(Unicode(100), comment="勘定科目名")
    kanjo_kamoku_group_code = Column(Integer, ForeignKey("m_kanjo_kamoku_group.kanjo_kamoku_group_code", ondelete="RESTRICT"), nullable=False, comment="勘定科目グループコード")
    version_id = Column(Integer, default=1, nullable=False, comment="バージョンID")
    created_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="作成日")
    updated_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="更新日")
    deleted_at = Column(Timestamp, default=current_timestamp(), comment="削除日")


