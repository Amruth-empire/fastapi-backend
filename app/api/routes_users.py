from fastapi import APIRouter
from app.schemas.user_schema import UserCreate, UserOut
from app.services.user_service import create_user, get_users

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=str)
def add_user(user: UserCreate):
    return create_user(user)

@router.get("/", response_model=list[UserOut])
def list_users():
    return get_users()
