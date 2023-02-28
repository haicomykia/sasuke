from sqlalchemy.orm import Session
from sqlalchemy import and_
from models.m_users import Users as mUser
from schemas.schemas import Users as sUser
from hash.hash import Hash


# ユーザー認証
def verify_user(db: Session, user: sUser) -> bool:
    result = db.query(mUser).filter(and_(mUser.deleted_at == None, \
                                        user.user_name == mUser.user_name)).first()
    if result is None:
        return False
    return Hash.verify_password(result.password, user.password)
