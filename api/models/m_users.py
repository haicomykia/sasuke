from sqlalchemy import Column, Integer, Text
from sqlalchemy import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp
from db.database import ModelBase


class Users(ModelBase):
    """
    ユーザーテーブル
    """
    __tablename__ = 'm_users'
    __table_args__ = {
        'comment': 'ユーザーマスタ'
    }

    user_id = Column(Integer, primary_key=True, autoincrement=True, comment="ユーザID", nullable=False)
    user_name = Column(Text, comment="ユーザー名", nullable=False)
    password = Column(Text, nullable=False, comment="パスワード")
    version_id = Column(Integer, default=1, nullable=False, comment="バージョンID")
    created_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="作成日")
    updated_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="更新日")
    deleted_at = Column(Timestamp, nullable=True, comment="削除日")
