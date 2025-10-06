## main.py


'''python # pyright: ignore[reportUndefinedVariable]
from fastapi import FastAPI # pyright: ignore[reportMissingImports]
from routes import users, courses, enrollments


app = FastAPI(title="EduTrack Lite API")


app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(enrollments.router, prefix="/enrollments", tags=["enrollments"])


@app.get("/")
def root():
    return {"msg": "EduTrack Lite API alive"}'''