from io import StringIO
from logging import getLogger

from fastapi import APIRouter, Depends, File, status, Response, UploadFile
import pandas as pd

from core.settings import Settings
from core.logger import logger as org_logger
from crud.auth import current_active_user
from models.user import User

settings = Settings()

org_logger.init_logger()
logger = getLogger(settings.LOG_LEVEL)

router = APIRouter()

@router.post('/uploadfile/', status_code=status.HTTP_200_OK)
async def upload_file(response: Response, file: UploadFile = File(...), \
                       user: User = Depends(current_active_user)) -> dict[str, str]:
    csvdata = StringIO(str(file.file.read(), 'utf-8'))
    df = pd.read_csv(csvdata)

    logger.info(f'{file.filename} has been read.')

    # ロジックはcrudモジュールに置く

    logger.info(csvdata.getvalue())
    response.status_code = status.HTTP_200_OK

    return {'filename': file.filename}