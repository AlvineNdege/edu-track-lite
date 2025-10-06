from fastapi import APIRouter, HTTPException, status # pyright: ignore[reportMissingImports]
from schemas.user import UserCreate, User
from services import user_service # pyright: ignore[reportAttributeAccessIssue]


router = APIRouter()


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate):
    return user_service.create_user(payload)


@router.get("/", response_model=list[User])
def list_users():
    return user_service.list_users()


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, payload: UserCreate):
    updated = user_service.update_user(user_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    ok = user_service.delete_user(user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="User not found")
    return None


@router.post("/{user_id}/deactivate", response_model=User)
def deactivate(user_id: int):
    user = user_service.deactivate_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user