from sqlalchemy import Column, Integer, Unicode, ForeignKey
from api.models.models import ModelBase


class AccountTitles(ModelBase):
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