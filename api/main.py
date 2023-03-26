from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session
from db.database import engine, get_db, ModelBase
from models import user_models
ModelBase.metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event('startup')
async def startup():
    await user_models.create_db_and_tables()
#
#
# @app.on_event('shutdown')
# async def shutdown():
#     await database.disconnect()
