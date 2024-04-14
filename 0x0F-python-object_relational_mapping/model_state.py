#!/usr/bin/python3
"""Class state definition"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """name and id attributes of each state"""

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
