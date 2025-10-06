from pydantic import BaseModel, EmailStr # pyright: ignore[reportMissingImports] #
from typing import Optional


class UserBase(BaseModel):
    name:str
    email:EmailStr


class UserCreate(UserBase):
    pass


class User(UserBase):
    id:int
    is_active:bool=True


class Config:
    orm_mode=True