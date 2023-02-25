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

    user_id = Column(Integer, primary_key=True, autoincrement=True, comment="ユーザーID")
    user_name = Column(Text, comment="ユーザーID", nullable=False)
    password = Column(Text, nullable=False, comment="パスワード")
