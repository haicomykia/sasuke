from sqlalchemy import Column, Integer, Unicode, String, DateTime, ForeignKey
from sqlalchemy import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp

from core.database import ModelBase
from models.base import Base

class Logs(ModelBase, Base):
    """
    操作ログテーブル
    """
    __tablename__ = 't_logs'
    __table_args__ = {
        'comment': '操作ログテーブル'
    }

    log_id = Column(Integer, primary_key=True, autoincrement=True, comment="ログID")
    sousa_type = Column(Integer, ForeignKey("m_sousa_types.sousa_id", ondelete="SET NULL"), comment="操作区分")
    program_id = Column(String, nullable=False, comment="プログラムID")
    operated_time = Column(DateTime, default=current_timestamp(), nullable=False, comment="操作日時")
    user_id = Column(String, nullable=False, comment="ユーザー名")
    message = Column(String, comment="メッセージ")