import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    contraseña = Column(String(250), nullable=False)
    idnumber = Column(Integer, nullable=False, primary_key=True)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(250))
    gravity = Column(String(250))
    terrain = Column(String(250))

    def to_dict(self):
        return {}
    
class Favorites(Base):
    __tablename__ = 'favorites'
    planets = Column(String(250), relationship(Planets))
    characters = Column(String(250), relationship(Characters))
    userID = Column(Integer, primary_key=True, nullable=False)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e