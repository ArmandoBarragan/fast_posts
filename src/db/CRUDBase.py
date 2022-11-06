# Typing
from typing import Generic
from typing import TypeVar
from typing import Type
from typing import Any
from typing import Optional
from typing import List

# pydantic
from pydantic import BaseModel

# SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import update

# FastAPI
from fastapi.encoders import jsonable_encoder

# Project
from src.settings import Base


""" Create classes that are accepted as parameters for the CRUDBase class"""
ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """ CRUD base class which contains the base methods Get, Read, Create and Update objects
    Methods: get, create, update, all.
    Parameters: SQLAlchemy model or Pydantic Schema. """
    def __init__(self, model: Type[ModelType]):
        """ Init sets the model of the class."""
        self.model = model

    def get(self, session: Session, id: Any) -> Optional[ModelType]:
        return session.query(self.model).filter(self.model.id == id).first()

    def all(self, session: Session) -> List[Any]:
        return session.query(self.model).all()

    def create(self, session: Session, object: CreateSchemaType) -> ModelType:
        object = self.model(**jsonable_encoder(object))
        session.add(object)
        session.commit()
        session.refresh(object)
        return object

    def update(self, session: Session, object: UpdateSchemaType) -> ModelType:
        object = session.query(self.model).\
            filter(object.id == self.model.id).update(**jsonable_encoder(object))
        session.commit()
        return object

