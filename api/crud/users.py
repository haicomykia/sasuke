import uuid
from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.db import SQLAlchemyUserDatabase
from core.settings import Settings
from db.database import get_user_db
from models.user import User

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    settings = Settings()
    reset_password_token_secret = settings.SECRET
    verification_token_secret = settings.SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User{user.id} has registered.")

    async def on_after_forget_password(self, token: str, user: User, request: Optional[Request] = None):
        print(f"User{user.id} has forget their password. Rest token: {token}")

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)