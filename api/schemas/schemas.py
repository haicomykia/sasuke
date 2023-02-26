from pydantic import BaseModel, Field


class Users(BaseModel):
    user_name: str = Field(max_length=20)
    password: str = Field(max_length=20)

    class Config:
        orm_mode = True
