from sqlalchemy.orm import Session
from models.m_users import Users as mUser
from models.schemas import Users as sUser


# ユーザー一覧を取得
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(mUser).offset(skip).limit(limit).all()


# ユーザー登録
def create_user(db: Session, user: sUser):
    new_user = mUser(user_name=user.user_name, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
