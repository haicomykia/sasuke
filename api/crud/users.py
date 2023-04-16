import uuid
from typing import Optional, Union

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin, InvalidPasswordException
from fastapi_users.db import SQLAlchemyUserDatabase

from core.settings import Settings
from db.database import get_user_db
from exceptions.error_message import Error_Message
from models.user import User
from schemas.schemas import UserCreate

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    settings = Settings()
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User{user.id} has registered.")

    async def on_after_forget_password(self, token: str, user: User, request: Optional[Request] = None):
        print(f"User{user.id} has forget their password. Rest token: {token}")

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")

    async def validate_password(self, password: str, user: Union[UserCreate, User]) -> None:
        password_len = 8
        if len(password) < password_len:
            raise InvalidPasswordException(
                reason=Error_Message.PASSWORD_NEEDS_AT_LEAST_STR_LEN.text.format(str(password_len))
            )

        capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        smallalphabets = "abcdefghijklmnopqrstuvwxyz"
        symbols = """ ~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/ """
        digits = "0123456789"

        cnt_cap, cnt_small, cnt_symbol, cnt_digit = 0, 0, 0, 0

        for i in password:
            if i in capitalalphabets:
                cnt_cap = cnt_cap + 1
            if i in smallalphabets:
                cnt_small = cnt_small + 1
            if i in symbols:
                cnt_symbol = cnt_symbol + 1
            if i in digits:
                cnt_digit = cnt_digit + 1

        if not(cnt_cap > 0 and cnt_small > 0 and cnt_digit > 0 and cnt_symbol > 0 \
                and cnt_cap + cnt_small + cnt_digit + cnt_symbol == len(password)):
            raise InvalidPasswordException(
                reason=Error_Message.INVALID_CHAR_TYPE_IN_PASSWORD.text
            )

        return None


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)