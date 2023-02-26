from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session
from schemas.schemas import Users
from db import database
from db.database import engine, get_db
import crud

database.ModelBase.metadata.create_all(bind=engine)

app = FastAPI()


# Create
@app.post('/users', response_model=Users)
async def create_users(user: Users, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


# Read
@app.get('/users', response_model=list[Users])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
