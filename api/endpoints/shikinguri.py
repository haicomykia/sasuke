from io import StringIO
from logging import getLogger

from fastapi import APIRouter, Depends, File, status, Response, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
import pandas as pd

from core.database import get_db
from core.settings import Settings
from core.logger import logger as org_logger
from crud.auth import current_active_user
from crud.sousa_log import add_sousa_log
from models.user import User
from schemas.schemas import LogsBase


settings = Settings()

org_logger.init_logger()
logger = getLogger(settings.LOG_LEVEL)

router = APIRouter()

@router.post('/uploadfile/', status_code=status.HTTP_200_OK)
async def upload_file(response: Response, file: UploadFile = File(...), \
                    user: User = Depends(current_active_user), \
                    db: AsyncSession = Depends(get_db)
                    ) -> dict[str, str]:
    csvdata = StringIO(str(file.file.read(), 'utf-8'))
    df = pd.read_csv(csvdata)

    # ロジックはcrudモジュールに置く
    logger.info(f'user_id:{user.email}')
    # 操作ログ
    log = LogsBase(
        program_id = __name__,
        user_id = user.email,
        message = f'{file.filename}を読み込みました。'
    )
    await add_sousa_log(db, log)

    response.status_code = status.HTTP_200_OK
    return {'filename': file.filename}

