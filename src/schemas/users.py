# Pydantic
from pydantic import BaseModel
from pydantic import Field

# Project
from src.db import CRUDBase
from src.models import UserAccount


class EmailMixin(BaseModel):
    email: str = Field(..., min_length=2, max_length=50)


class PasswordMixin(BaseModel):
    password: str = Field(..., min_length=8, max_length=60)


class UserMixin(EmailMixin):
    first_name: str = Field(..., min_length=2, max_length=30)
    last_name: str = Field(..., min_length=2, max_length=50)


class CreateAccountSchema(UserMixin, PasswordMixin):
    pass


class ReturnUserSchema(UserMixin):
    id: int

    class Config:
        orm_mode=True

class LoginSchema(EmailMixin, PasswordMixin):
    pass


class UpdateUserSchema(UserMixin):
    id: int
    class Config:
        orm_mode=True


class CRUDUserAccount(CRUDBase[UserAccount, CreateAccountSchema, UpdateUserSchema]):
    """Inherits from CRUDBase to make UserAccounts operations"""
    pass


crud_users = CRUDUserAccount(UserAccount)