# SQLAlchemy
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Boolean

# Project
from src.settings import Base


class UserAccount(Base):
    """ User model"""
    __tablename__ = 'user_accounts'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(60))
    email = Column(String(60))
    password = Column (String(60))