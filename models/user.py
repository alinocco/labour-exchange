from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    hashed_password: str
    is_company: bool
    created_date: datetime
    changed_date: datetime

class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)
    confirm_password: str
    is_company: bool = False

    @validator("confirm_password")
    def password_match(cls, value, values, **kwargs):
        if "password" in values and value != values["password"]:
            raise ValueError("Passwords don't match.")
        return value

class UserOut(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    is_company: bool
    created_date: datetime
    changed_date: datetime

