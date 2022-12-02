import os
from sqlalchemy import Column, Integer, Unicode
from api.models.models import ModelBase


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