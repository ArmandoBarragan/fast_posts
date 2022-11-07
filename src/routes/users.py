# FastAPI
from fastapi import APIRouter

# Project
from src.schemas import crud_users
from src.schemas import CreateAccountSchema
from src.schemas import LoginSchema
from src.schemas import ReturnUserSchema
from src.schemas import UpdateUserSchema
from src.db import Session


router = APIRouter()


# Routes
@router.post('/users/create_account',
             tags=['auth'])
def create_account():
    return 'hi'


@router.get('/users/{user_id}',
            tags=['users'])
def user_detail(user_id: int):
    return 'hi'


@router.post('/users/logout',
             tags=['auth'])
def logout():
    return 'hi'


@router.patch('/users/{user_id}',
              tags=['users'])
def update_user(user_id: int):
    return 'hi'


@router.delete('/users/{user_id}',
               tags=['auth'])
def delete_user(user_id: int):
    return 'hi'