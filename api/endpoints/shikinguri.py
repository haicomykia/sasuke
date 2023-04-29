from io import StringIO
from logging import getLogger
from fastapi import APIRouter, Depends, File, status, Response, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
import pandas as pd
from core.database import get_db
from core.settings import Settings
from core.logger import logger as org_logger
from crud.auth import current_active_user
from crud.sousa_log import add_sousa_log
from enums.sousa_types import SousaTypesEnum
from exceptions.core import APIException, SystemException
from models.user import User
from schemas.schemas import LogsBase

settings = Settings()

org_logger.init_logger()
logger = getLogger(settings.LOG_LEVEL)

router = APIRouter()


@router.post('/log/')
async def write_log(log: LogsBase, \
                    user: User = Depends(current_active_user), \
                    db: AsyncSession = Depends(get_db)):
    try:
        await add_sousa_log(db, log)
    except APIException as se:
        logger.error(se)
        raise APIException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                           message=se.message)
    except Exception as e:
        logger.error(e)
        raise SystemException(e)

    res = JSONResponse(content={'detail': True})
    res.status_code = status.HTTP_201_CREATED
    return res


@router.post('/uploadfile/')
async def upload_file(file: UploadFile = File(...), \
                      user: User = Depends(current_active_user), \
                      db: AsyncSession = Depends(get_db)
                      ) -> dict[str, str]:
    csvdata = StringIO(str(file.file.read(), 'utf-8'))
    df = pd.read_csv(csvdata)

    # ロジックはcrudモジュールに置く

    # 操作ログ
    log = LogsBase(
        sousa_type=SousaTypesEnum.ENTRY.sousa_id,
        program_id=__name__,
        user_id=user.email,
        message=f'ファイル名：{file.filename}'
    )

    try:
        await add_sousa_log(db, log)
    except APIException as se:
        logger.error(se)
        raise APIException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                           message=se.message)
    except Exception as e:
        logger.error(e)
        raise SystemException(e)

    res = JSONResponse(content={'detail': file.filename})
    res.status_code = status.HTTP_200_OK
    return res
