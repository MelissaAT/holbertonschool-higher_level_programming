#!/usr/bin/python3
"""Write a python file that contains the class
definition of STate and an instance"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """Class State"""
    __states__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
