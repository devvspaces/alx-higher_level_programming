#!/usr/bin/python3
"""
This script defines a City class
using SQLAlchemy ORM
it has a relationship with the State class
"""
from sqlalchemy import Column, ForeignKey, Integer, String

from model_state import Base


class City(Base):
    """
    City class inherits from Base

    :param Base: Base class
    :type Base: class

    Attributes:
    :param id: id of the city
    :type id: int
    :param state_id: id of the state
    :type state_id: int
    :param name: name of the city
    :type name: str
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
