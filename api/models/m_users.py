import os
from sqlalchemy import Column, Integer, Text
from models.models import ModelBase

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
