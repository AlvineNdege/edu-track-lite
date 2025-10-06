from pydantic import BaseModel # pyright: ignore[reportMissingImports]
from typing import Optional


class CourseBase(BaseModel):
    title:str
    description:Optional[str]

class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id:int
    is_open:bool=True


class Config:
    orm_mode=True