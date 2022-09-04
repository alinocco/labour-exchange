from typing import List
from fastapi import APIRouter, Depends

from repositories.users import UserRepository
from models.user import User, UserIn, UserOut
from .depends import get_user_repository

router = APIRouter()

@router.get("/", response_model=List[UserOut])
async def read_users(
    users: UserRepository = Depends(get_user_repository),
    limit: int = 100, 
    skip: int = 0):
    return await users.get_all(limit=limit, skip=skip)

@router.post("/", response_model=UserOut)
async def create_user(
    user: UserIn,
    users: UserRepository = Depends(get_user_repository)):
    return await users.create(user=user)
