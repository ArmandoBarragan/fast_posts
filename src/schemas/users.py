from pydantic import BaseModel
from pydantic import Field


class UserMixin(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=30)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(..., min_length=2, max_length=50)


class CreateAccountSchema(UserMixin):
    password: str = Field(..., min_length=8, max_length=60)
    class Config:
        orm_mode=True

class ReturnUserSchema(UserMixin):
    id: int
