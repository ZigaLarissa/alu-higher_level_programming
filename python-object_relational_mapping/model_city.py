#!/usr/bin/python3
"""Contains a class definition of a City(a class)
and an instance Base = declarative_base()."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


"""Create a new base class from which all mapped classes should inherit."""
Base = declarative_base()


class City(Base):
    """A class defining a Table in sql."""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
