from pydantic import BaseModel # pyright: ignore[reportMissingImports]
from datetime import date


class EnrollmentBase(BaseModel):
    user_id:int
    course_id:int


class EnrollmentCreate(EnrollmentBase):
    pass


class Enrollment(EnrollmentBase):
    id:int
    enrolled_date:date
    completed:bool=False


class Config:
    orm_mode=True