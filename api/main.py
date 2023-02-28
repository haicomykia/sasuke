from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session
from schemas.schemas import Users
from db import database
from db.database import engine, get_db
import logic.user as userLogic
import logic.auth as authLogic

database.ModelBase.metadata.create_all(bind=engine)

app = FastAPI()


# Create
@app.post('/user', response_model=Users)
async def create_users(user: Users, db: Session = Depends(get_db)):
    return userLogic.create_user(db=db, user=user)


# Read
@app.get('/user', response_model=list[Users])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = userLogic.get_users(db=db, skip=skip, limit=limit)
    return users


# User Auth
@app.post('/user/auth')
async def verify_user(user: Users, db: Session = Depends(get_db)) -> bool:
    return authLogic.verify_user(db=db, user=user)
