import sys, os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.environ['DB_URL'])

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

ModelBase = declarative_base()