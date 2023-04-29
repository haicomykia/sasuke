import asyncio
from logging import getLogger
from sqlalchemy.sql import text
from sqlalchemy.exc import IntegrityError
from core.database import session_factory
from core.settings import Settings
from core.logger import logger as org_logger
from enums.sousa_types import SousaTypesEnum
from exceptions.error_message import Error_Message
from models.m_sousa_types import SousaTypes

async def main():
    """
    操作区分マスタを洗い替え
    """
    settings = Settings()
    org_logger.init_logger()
    logger = getLogger(__name__)

    if settings.ENV != 'local':
        logger.info(Error_Message.EXECUTE_LOCAL_ENV_ONLY.text)
        return None

    db = session_factory()

    await db.execute(text(f'DELETE FROM {SousaTypes.__tablename__}'))
    await db.commit()


    sousa_types = (SousaTypes(sousa_id=each.sousa_id, sousa_name=each.sousa_name) \
                   for each in SousaTypesEnum)
    db.add_all(list(sousa_types))

    try:
        await db.flush()
        await db.commit()
        await db.close()
    except IntegrityError as e:
        await db.rollback()
        logger.error(Error_Message.DB_INSERT_ERROR.text)
        raise e

    return sousa_types


if __name__ == "__main__":
   loop = asyncio.get_event_loop()
   loop.run_until_complete(main())

