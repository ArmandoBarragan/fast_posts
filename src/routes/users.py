# FastAPI
from fastapi import APIRouter
from fastapi import status
from fastapi import HTTPException

# SQLAlchemy
from sqlalchemy.exc import NoResultFound

# Project schemas
from src.schemas import crud_users
from src.schemas import CreateAccountSchema
from src.schemas import LoginSchema
from src.schemas import ReturnUserSchema
from src.schemas import UpdateUserSchema

# Project encryption
from src.utils.passwords import hash_password
from src.utils.passwords import check_password

# Project DB
from src.models import UserAccount
from src.db import Session

router = APIRouter()


# Routes
@router.post('/users/create_account',
             tags=['auth'],
            response_model=ReturnUserSchema)
def create_account(account: CreateAccountSchema):
    """
    Creates a UserAccount after confirming the user doesn't already exist and encrypting the password
    :param account: CreateAccountSchema.
    :return: ReturnUserSchema.
    """
    # TODO: Validators
    with Session() as session:
        existing_account = crud_users.email_query(session, account.email)

        if existing_account is not None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                 detail="Account already exists")

        verified_account = account
        verified_account.password = hash_password(account.password)

        account = crud_users.create(session=session, object=account)

        return account


@router.post('/users/login',
             tags=['auth'])
def login(credentials: LoginSchema):
    """
    Check's the user's credentials and returns a SuccessfulLoginSchema if they're valid; returns HttpException
    if they're not
    :param credentials: LoginSchema.
    :return: SuccessfulLoginSchema or HttpException.
    """
    # TODO create SuccessfulLoginSchema.
    with Session() as session:
        user = crud_users.email_query(session, credentials.email)

        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="This user was not found.")

        if check_password(credentials.password, user.password):
            return "Logged in"

        return "Your password is incorrect."



@router.get('/users/{user_id}',
            tags=['users'],
            status_code=status.HTTP_204_NO_CONTENT)
def user_detail(user_id: int):
    """
    :param user_id: int
    :return: HttpStatus
    """
    with Session() as session:
        crud_users.delete(session, user_id)
        return {"response": "deleted"}


@router.post('/users/logout',
             tags=['auth'])
def logout():
    return 'hi'


@router.patch('/users/{user_id}',
              tags=['users'],
              response_model=ReturnUserSchema)
def update_user(update_object: UpdateUserSchema, password):
    """
    Takes a password and an UpdateUserSchema, checks if the account exists and the password matches, then
    updates the database record.
    :param user_id: int
    :param update_object: UpdateUserSchema
    :param password: str
    :return: ReturnUserSchema
    """
    with Session() as session:
        account = crud_users.get(session, update_object.id)

        if account and check_password(password, account.password):
            return crud_users.update(session, update_object)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="There's no user with this id.")


@router.delete('/users/{user_id}',
               tags=['users'],
               status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    with Session() as session:
        delete_message = crud_users.delete(session, user_id)
        return {"detail": delete_message}