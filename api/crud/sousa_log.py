import traceback
from logging import getLogger
from fastapi import status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.settings import Settings
from core.logger import logger as org_logger
from exceptions.core import APIException, SystemException
from models.t_logs import Logs
from schemas.schemas import LogsBase
from enums.sousa_types import SousaTypesEnum

settings = Settings()

org_logger.init_logger()
logger = getLogger(settings.LOG_LEVEL)

async def add_sousa_log(db: AsyncSession, request: LogsBase) -> Logs:
    """
    操作ログを記録
    Parameters
    ----------
    db: AsyncSession
        DBセッション
    request: LogBase
        操作ログの登録項目

    Returns
    -------
    new_log: Logs
        登録後の操作ログ
    """

    if request.sousa_type not in tuple(each.sousa_id for each in SousaTypesEnum):
        message = f'存在しない操作区分です。details={request.sousa_type}'
        logger.error(message)
        raise APIException(message=message,
                           status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


    new_log = Logs(**request.dict())

    try:
        db.add(new_log)
        await db.commit()
    except Exception as e:
        await db.rollback()
        logger.error(e)
        raise SystemException(e)

    await db.refresh(new_log)
    return new_log