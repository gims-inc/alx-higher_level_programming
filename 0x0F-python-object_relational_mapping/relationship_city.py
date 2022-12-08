#!/usr/bin/python3
"""
Defines a City model
Inherits from SQLAlchemy Base and links tothe MySql table states.
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a state for a MySQL database.
    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Column): The city's id.
    name (sqlalchemy.Column): The city's name.
    states_id(sqlalchemy.Column): FK
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
