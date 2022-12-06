#!/usr/bin/python3
"""Contains a class definition of a state(a class)
and an instance Base = declarative_base()."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


"""Create a new base class from which all mapped classes should inherit."""
Base = declarative_base()


class State(Base):
    """A class defining a Table in sql."""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(128), nullable=False)
