from sqlalchemy import Column, Integer, Unicode, ForeignKey
from sqlalchemy import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp

from core.database import ModelBase
from models.base import Base


class AccountTitles(ModelBase, Base):
    """
    勘定科目マスタ
    """
    __tablename__ = 'm_kanjo_kamoku'
    __table_args__ = {
        'comment': '勘定科目マスタ'
    }

    kanjo_kamoku_id = Column(Integer, primary_key=True, autoincrement=True, comment="勘定科目ID")
    kanjo_kamoku_name = Column(Unicode(100), comment="勘定科目名")
    kanjo_kamoku_group_code = Column(Integer, ForeignKey("m_kanjo_kamoku_groups.kanjo_kamoku_group_code", ondelete="RESTRICT"), nullable=False, comment="勘定科目グループコード")
    version_id = Column(Integer, default=1, nullable=False, comment="バージョンID")
    created_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="作成日")
    updated_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="更新日")
    deleted_at = Column(Timestamp, nullable=True, comment="削除日")
