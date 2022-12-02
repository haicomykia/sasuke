from sqlalchemy import Column, Integer, Unicode
from api.models.models import ModelBase


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