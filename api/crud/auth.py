import uuid
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy
)
import crud.users as user_crud
from models.user import User

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret = user_crud.SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name = "jwt",
    transport = bearer_transport,
    get_strategy = get_jwt_strategy
)


fastapi_users = FastAPIUsers[User, uuid.UUID](user_crud.get_user_manager, [auth_backend])
current_active_user = fastapi_users.current_user(active=True)