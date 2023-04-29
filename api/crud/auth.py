import uuid
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy
)
from core.settings import Settings
import crud.users as user_crud
from models.user import User


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
settings = Settings()

def get_jwt_strategy() -> JWTStrategy:
    EXPIRED_SECONDS = 60 * 30
    return JWTStrategy(secret = settings.SECRET_KEY, lifetime_seconds=EXPIRED_SECONDS)

auth_backend = AuthenticationBackend(
    name = "jwt",
    transport = bearer_transport,
    get_strategy = get_jwt_strategy
)

fastapi_users_at_auth = FastAPIUsers[User, uuid.UUID](user_crud.get_user_manager, [auth_backend])
current_active_user = fastapi_users_at_auth.current_user(active=True)