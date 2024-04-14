#!/usr/bin/python3
"""state class and Base"""

from sqlalchemy import MetaData, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

medata = MetaData()
Base = declarative_base(metadata=medata)

class State(Base):
    """name and id attributes of each state"""
    __tablename__= 'states'
    name = Column(String(128), nullable=False)
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
