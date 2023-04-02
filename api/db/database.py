import sys, os
# from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from dotenv import load_dotenv

load_dotenv()

# echo=True
DATABASE_URL = os.environ['DB_URL']
ModelBase = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=True)
# ModelBase.metadata.create_all(engine)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
