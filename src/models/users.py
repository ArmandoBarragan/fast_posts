from sqlalchemy import String, Integer, Column, ForeignKey, Boolean

from src.settings.settings import Base



class UserAccount(Base):
    __tablename__ = 'user_accounts'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(60))
    email = Column(String(60))
    password = Column (String(60))