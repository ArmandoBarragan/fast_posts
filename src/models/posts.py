# SQLAlchemy
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Boolean
from sqlalchemy.dialects.postgresql import TEXT

# Project
from src.settings import Base

class Post(Base):
    """ Post model"""
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(TEXT)
    author_pk = Column(Integer, ForeignKey('user_accounts.id'))

