from fastapi import APIRouter, HTTPException, status # pyright: ignore[reportMissingImports]
from schemas.enrollment import EnrollmentCreate, Enrollment
from services import enrollment_service


router = APIRouter()


@router.post("/", response_model=Enrollment, status_code=status.HTTP_201_CREATED)
def enroll(payload: EnrollmentCreate):
    try:
     e = enrollment_service.enroll(payload)
     return e
    except: ValueError ;a # pyright: ignore[reportUnusedExpression, reportUndefinedVariable]a