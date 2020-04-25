from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
Usamos sqlalchemy ya que nos abstrae del tipo de sql especifico mediante un ORM
Object Relationship Model
"""

engine = create_engine('sqlite:///newspaper.db')

Session = sessionmaker(bind=engine)

Base = declarative_base()
