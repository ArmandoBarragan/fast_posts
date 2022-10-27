from sqlalchemy import String, Integer, Column, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import TEXT
from src.settings.settings import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(TEXT)
    author_pk = Column(Integer, ForeignKey('user_accounts.id'))