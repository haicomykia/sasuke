from logging import getLogger

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, scoped_session

from core.settings import Settings
from core.logger import logger as org_logger

settings = Settings()

org_logger.init_logger()
logger = getLogger(__name__)

ModelBase = declarative_base()

try:
    engine = create_async_engine(settings.DB_URL, echo=True)
    logger.info(engine)
    session_factory = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession))
except Exception as e:
    logger.error(f"DB connection error. detail={e}")

async def get_db():
    async with session_factory() as session:
        yield session

# def get_db():
#     db = session_factory()
#     try:
#         yield db
#     finally:
#         db.close()