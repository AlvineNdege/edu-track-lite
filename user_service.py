from typing import Dict, List, Optional
from schemas.user import User, UserCreate


_users: Dict[int, User] = {}
_next_id = 1




def list_users() -> List[User]:
    return list(_users.values())




def get_user(user_id: int) -> Optional[User]:
    return _users.get(user_id)




def create_user(payload: UserCreate) -> User:
    global _next_id
    user = User(id=_next_id, name=payload.name, email=payload.email, is_active=True)
    _users[_next_id] = user
    _next_id += 1
    return user




def update_user(user_id: int, payload: UserCreate) -> Optional[User]:
    user = _users.get(user_id)
    if not user:
        return None
    user.name = payload.name
    user.email = payload.email
    _users[user_id] = user
    return user




def delete_user(user_id: int) -> bool:
    return _users.pop(user_id, None) is not None




def deactivate_user(user_id: int) -> Optional[User]:
    user = _users.get(user_id)
    if not user:
        return None
    user.is_active = False
    _users[user_id] = user
    return user