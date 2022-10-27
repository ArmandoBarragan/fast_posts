from pydantic import BaseModel
from pydantic import Field


class EmailMixin(BaseModel):
    email: str = Field(..., min_length=2, max_length=50)


class PasswordMixin(BaseModel):
    password: str = Field(..., min_length=8, max_length=60)


class UserMixin(EmailMixin):
    first_name: str = Field(..., min_length=2, max_length=30)
    last_name: str = Field(..., min_length=2, max_length=50)


class CreateAccountSchema(UserMixin, PasswordMixin):
    class Config:
        orm_mode=True


class ReturnUserSchema(UserMixin):
    id: int


class LoginSchema(EmailMixin, PasswordMixin):
    pass
