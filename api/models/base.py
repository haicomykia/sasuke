from sqlalchemy import Column, Integer, Unicode, ForeignKey
from sqlalchemy import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp


class Base:
    """
    共通カラム
    """
    version_id = Column(Integer, default=1, nullable=False, comment="バージョンID")
    created_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="作成日")
    updated_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="更新日")
    deleted_at = Column(Timestamp, nullable=True, comment="削除日")