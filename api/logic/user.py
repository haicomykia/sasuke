from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import current_timestamp
from hash.hash import Hash
from models import m_users
from schemas import schemas
from . import auth


# 　ユーザー一覧を取得
def get_users(db: Session, skip: int = 0, limit: int = 100) -> m_users.Users:
    return db.query(m_users.Users).filter(m_users.Users.deleted_at == None) \
        .offset(skip).limit(limit).all()


# ユーザー登録
def create_user(db: Session, user: schemas.Users) -> m_users.Users:
    new_user = m_users.Users(user_name=user.user_name,
                    password=Hash.get_password_hash(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# 退会
def leave_user(db: Session, user: schemas.Users) -> bool:
    old_user = db.query(m_users.Users).filter(
        and_(m_users.Users.deleted_at == None,
            user.user_name == m_users.Users.user_name)
        ).first()

    if old_user is None:
        return False

    if not auth.verify_user(db, user):
        return False

    old_user.deleted_at = current_timestamp()
    db.commit()

    return True
