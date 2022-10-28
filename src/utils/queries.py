from typing import TypeVar

# Sqlalchemy
from sqlalchemy import Column

# Database
from src.settings.db import Session
from src.settings.settings import Base


Table = TypeVar(Base)


# Query Methods
def all(table: Table):
    """ Method to return all records."""
    with Session() as session:
        return session.query(table)


def filter(table: Table, column: Column, operation, value):
    """ Method to make a WHERE query"""
    with Session() as session:
        return session.query(table)


def get(table: Table, column: Column, value):
    with Session() as session:
        return session.query(table)
