from fastapi import APIRouter, Depends, Form, HTTPException, status, Response

from core.hasher import verify_password
from crud.auth import fastapi_users_at_auth, auth_backend, current_active_user
from exceptions.error_message import Error_Message
from models.user import User


router = APIRouter()

@router.post('/authenticate', status_code=status.HTTP_200_OK)
async def authenticate(response: Response, plain_password: str = Form(), user: User = Depends(current_active_user)) -> dict[str, str]:
    if not verify_password(plain_password, user.hashed_password):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'detail': Error_Message.INCORRECT_PASSWORD.text}

    response.status_code = status.HTTP_200_OK
    return {'detail': ''}