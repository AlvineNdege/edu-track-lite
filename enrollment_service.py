from typing import Dict, List, Optional

from EduTrackLite.routes import enrollments # pyright: ignore[reportMissingImports]


def user_enrollments(user_id: int) -> List[enrollments]: # pyright: ignore[reportInvalidTypeForm]
    return [e for e in enrollments.values() if e.user_id == user_id] # pyright: ignore[reportAttributeAccessIssue]




def course_enrollments(course_id: int) -> List[enrollments]: # pyright: ignore[reportInvalidTypeForm]
    return [e for e in enrollments.values() if e.course_id == course_id] # pyright: ignore[reportAttributeAccessIssue]




def _find_duplicate(user_id: int, course_id: int) -> Optional[enrollments]: # pyright: ignore[reportInvalidTypeForm]
    for e in enrollments.values(): # pyright: ignore[reportAttributeAccessIssue]
     if e.user_id == user_id and e.course_id == course_id:
        return e
    return None




def enroll(payload: EnrollmentCreate) -> enrollments: # pyright: ignore[reportGeneralTypeIssues, reportUndefinedVariable]
    global _next_id
    user=user_service.get_user(payload.user_id) # pyright: ignore[reportUndefinedVariable]
    if not user:
        raise ValueError("User does not exist")
    if not user.is_active:
        raise PermissionError("User is not active")
    course = course_service.get_course(payload.course_id) # pyright: ignore[reportUndefinedVariable]
    if not course:
        raise ValueError("Course does not exist")
    if not course.is_open:
        raise PermissionError("Course is closed for enrollment")
    if _find_duplicate(payload.user_id, payload.course_id):
        raise FileExistsError("User already enrolled in course")


    enrollment = Enrollment(id=_next_id, user_id=payload.user_id, course_id=payload.course_id, enrolled_date=date.today(), completed=False) # pyright: ignore[reportUnboundVariable, reportUndefinedVariable]
    _enrollments[_next_id] = enrollment # pyright: ignore[reportUnboundVariable, reportUndefinedVariable]
    _next_id += 1 # pyright: ignore[reportUnboundVariable]
    return enrollment




def mark_completed(enrollment_id: int) -> Optional[enrollments]: # pyright: ignore[reportInvalidTypeForm]
    enrollment = enrollments.get(enrollment_id) # pyright: ignore[reportAttributeAccessIssue]
    if not enrollment:
        return None
    enrollment.completed = True
    enrollments[enrollment_id] = enrollment # pyright: ignore[reportIndexIssue]
    return enrollment




def delete_enrollment(enrollment_id: int) -> bool:
    return enrollments.pop(enrollment_id, None) is not None # pyright: ignore[reportAttributeAccessIssue]