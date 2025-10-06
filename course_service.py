from typing import Dict, List, Optional
from schemas.course import Course, CourseCreate


_courses: Dict[int, Course] = {}
_next_id = 1




def list_courses() -> List[Course]:
    return list(_courses.values())




def get_course(course_id: int) -> Optional[Course]:
    return _courses.get(course_id)




def create_course(payload: CourseCreate) -> Course:
    global _next_id
    course = Course(id=_next_id, title=payload.title, description=payload.description or "", is_open=True)
    _courses[_next_id] = course
    _next_id += 1
    return course




def update_course(course_id: int, payload: CourseCreate) -> Optional[Course]:
    course = _courses.get(course_id)
    if not course:
         return None
    course.title = payload.title
    course.description = payload.description or ""
    _courses[course_id] = course
    return course




def delete_course(course_id: int) -> bool:
    return _courses.pop(course_id, None) is not None




def close_enrollment(course_id: int) -> Optional[Course]:
    course = _courses.get(course_id)
    if not course:
        return None
    course.is_open = False
    _courses[course_id] = course
    return course