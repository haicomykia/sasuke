from sqlalchemy import Column, Integer, Unicode
from sqlalchemy import TIMESTAMP as Timestamp
from sqlalchemy.sql.functions import current_timestamp
from db.database import ModelBase


class SalaryTypes(ModelBase):
    """
    給与種別マスタ
    """
    __tablename__ = 'm_salary_types'
    __table_args__ = {
        'comment': '給与種別マスタ'
    }

    salary_type_id = Column(Integer, primary_key=True, autoincrement=True, comment="給与種別ID")
    name = Column(Unicode(10), comment="名称")
    created_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="作成日")
    updated_at = Column(Timestamp, default=current_timestamp(), nullable=False, comment="更新日")
    deleted_at = Column(Timestamp, nullable=True, comment="削除日")
