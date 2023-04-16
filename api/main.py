import os
from logging import getLogger

from fastapi import FastAPI, Depends, Form

from core.settings import Settings
from core.logger import logger as org_logger
from crud.auth import fastapi_users_at_auth, auth_backend, current_active_user
from endpoints import auth
from models.user import User
from schemas.schemas import UserRead, UserCreate, UserUpdate

org_logger.init_logger()
logger = getLogger(__name__)

settings = Settings()
app = FastAPI(
    title=f"{settings.ENV}{settings.TITLE}",
)


app.include_router(
    fastapi_users_at_auth.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)


app.include_router(
    fastapi_users_at_auth.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags = ["auth"]
)


app.include_router(
    fastapi_users_at_auth.get_reset_password_router(),
    prefix="/user",
    tags=["user"]
)


app.include_router(
    fastapi_users_at_auth.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"]
)



app.include_router(
    fastapi_users_at_auth.get_users_router(UserRead, UserUpdate),
    prefix="/user",
    tags=["user"]
)


app.include_router(
    auth.router,
    prefix="/auth",
    tags=["auth"]
)


@app.get('/')
def index(user: User = Depends(current_active_user)):
    logger.error('This is Info Message.')
    return {'result', __name__}