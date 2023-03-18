from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session
from schemas.schemas import Users
from models import m_users
from db import database
from db.database import engine, get_db
import logic.user as user_logic
import logic.auth as auth_logic

database.ModelBase.metadata.create_all(bind=engine)

app = FastAPI()


# Create
@app.post('/user', response_model=Users)
async def create_user(user: Users, db: Session = Depends(get_db)) -> m_users.Users:
    return user_logic.create_user(db=db, user=user)


# Read
@app.get('/user', response_model=list[Users])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> m_users.Users:
    users = user_logic.get_users(db=db, skip=skip, limit=limit)
    return users


# User Auth
@app.post('/user/auth')
async def authorize_user(user: Users, db: Session = Depends(get_db)) -> bool:
    return auth_logic.verify_user(db=db, user=user)

# Leave User
@app.post('/user/leave')
async def leave_user(user: Users, db: Session = Depends(get_db)) -> bool:
    return user_logic.leave_user(db=db, user=user)
