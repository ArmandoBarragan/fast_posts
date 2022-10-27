# FastAPI
from fastapi import APIRouter

# Models
from src.models.users import UserAccount

# Schemas
from src.schemas.users import ReturnUserSchema
from src.schemas.users import CreateAccountSchema


router = APIRouter()


# Routes
@router.post('/create/')
def create_account():
    pass


@router.get('/{user_id}')
def get_user(user_id: int):
    pass


@router.post('/login/')
def login():
    pass