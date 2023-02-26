from sqlalchemy.orm import Session
from models.m_users import Users as mUser
from schemas.schemas import Users as sUser
from models.models import ModelBase
from hash.hash import Hash


# ユーザー一覧を取得
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(mUser).filter(mUser.deleted_at == None)\
            .offset(skip).limit(limit).all()


# ユーザー登録
def create_user(db: Session, user: sUser):
    new_user = mUser(user_name=user.user_name, password=Hash.get_password_hash(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
