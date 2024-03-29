from typing import Optional
import uuid
from pydantic import BaseModel
from fastapi_users import schemas

class UserRead(schemas.BaseUser[uuid.UUID]):
    user_name: str

class UserCreate(schemas.BaseUserCreate):
    user_name: str


class UserUpdate(schemas.BaseUserUpdate):
    user_name: Optional[str]

class LogsBase(BaseModel):
    log_id: Optional[int]
    sousa_type: int
    program_id: str
    user_id: str
    message: str

    class Config:
        orm_mode = True