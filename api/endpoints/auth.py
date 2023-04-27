from fastapi import APIRouter, Depends, Form, HTTPException, status, Response
from fastapi.responses import JSONResponse
from core.hasher import verify_password
from crud.auth import fastapi_users_at_auth, auth_backend, current_active_user
from exceptions.core import APIException
from exceptions.error_message import Error_Message
from models.user import User

router = APIRouter()

@router.post('/authenticate')
async def authenticate(plain_password: str = Form(),
                       user: User = Depends(current_active_user)) -> dict[str, bool]:
    if not verify_password(plain_password, user.hashed_password):
        message = Error_Message.INCORRECT_PASSWORD.text
        raise APIException(message=message)

    res = JSONResponse(content={'detail': True})
    res.status_code = status.HTTP_200_OK
    return res