from sqlalchemy import Column, Integer, Unicode
from sqlalchemy import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp
from db.database import ModelBase


class AccountTitleGroups(ModelBase):
    """
    勘定科目グループマスタ
    """
    __tablename__ = 'm_kanjo_kamoku_groups'
    __table_args__ = {
        'comment': '勘定科目グループマスタ'
    }

    kanjo_kamoku_group_code = Column(Integer, primary_key=True, autoincrement=True, comment="勘定科目グループコード")
    group_name = Column(Unicode(100), comment="勘定科目名")
    created_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="作成日")
    updated_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="更新日")
    deleted_at = Column(Timestamp, nullable=True, comment="削除日")
