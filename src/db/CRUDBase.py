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
        """
        Returns an instance of the record that matches the id.
        :param session: Session
        :param id: int
        :return: Model
        """
        return session.query(self.model).filter(self.model.id == id).first()

    def all(self, session: Session) -> List[Any]:
        """
        Returns a list of all records in the table.
        :param session: Session
        :return: List[Model]
        """
        return session.query(self.model).all()

    def create(self, session: Session, object: CreateSchemaType) -> ModelType:
        """
        Creates in the database a new record of the table and returns the object.
        :param session: Session
        :param object: CreateSchemaType
        :return: Object
        """
        object = self.model(**jsonable_encoder(object))
        session.add(object)
        session.commit()
        session.refresh(object)
        return object

    def update(self, session: Session, object: UpdateSchemaType):
        """
        Takes an UpdateSchemaType object, updates the record and returns the refreshed object.
        :param session: Session
        :param object: UpdateSchemaType
        :return: Model
        """
        session.query(self.model).\
            filter(self.model.id == object.id).update({**jsonable_encoder(object)})
        session.commit()

        return self.get(session, object.id)

    def delete(self, session: Session, id: int) -> str:
        """Deletes a record that matches the id."""
        session.query(self.model).filter(self.model.id == id).delete()
        session.commit()
        return "{} with id {} deleted".format(self.model, id)

