from fastapi import FastAPI, Depends
from models.user import User
from crud.auth import fastapi_users, auth_backend, current_active_user
from schemas.schemas import UserRead, UserCreate, UserUpdate

app = FastAPI()


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags = ["auth"]
)


app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/user",
    tags=["user"]
)


app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"]
)



app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/user",
    tags=["user"]
)


@app.get('/')
def index(user: User = Depends(current_active_user)):
    return {'message', f"{user.email}"}