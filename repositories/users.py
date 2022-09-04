from datetime import datetime
from typing import List, Optional

from .base import BaseRepository
from core.security import hash_password, verify_password

from db.users import users
from models.user import User, UserIn, UserOut

class UserRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[UserOut]:
        query = users.select().limit(limit).offset(skip)
        user_list = await self.database.fetch_all(query=query)
        return user_list

    async def get_by_id(self, id: int) -> Optional[UserOut]:
        query = users.select().where(users.c.id==id).first()
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return UserOut.parse_obj(user)

    async def get_by_email(self, email: str) -> Optional[UserOut]:
        query = users.select().where(users.c.email==email).first()
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return UserOut.parse_obj(user)

    async def create(self, user: UserIn) -> UserOut:
        user = User(
            name=user.name,
            email=user.email,
            hashed_password=hash_password(user.password),
            is_company=user.is_company,
            created_date=datetime.utcnow(),
            changed_date=datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop("id", None)


        query = users.insert().values(**values)
        user.id = await self.database.execute(query=query)
        return user

    async def update(self, id: int, user: UserIn) -> UserOut:
        user = User(
            id=id,
            name=user.name,
            email=user.email,
            hashed_password=hash_password(user.password),
            is_company=user.is_company,
            created_date=datetime.utcnow(),
            changed_date=datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop("id", None)
        values.pop("created_date", None)

        query = users.update().where(users.c.id==id).values(**values)
        await self.database.execute(query=query)
        return user
