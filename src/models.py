import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Last_name = Column(String(250), nullable=False)
    User = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    Subscription_date = Column(String(250), nullable=False)
    user = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Starships(Base):
    __tablename__ = 'starships'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(250))
    model = Column(String(250))
    crew = Column(String(250), nullable=False)
    hyperdrive_rating = Column(String(250))
    lenght = Column(String(250))
    Starships_id = Column(Integer, ForeignKey('favorites'))
    favorites = relationship ("Favorites", back_populates =  "planets")

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(250))
    populations = Column(String(250))
    gravity = Column(String(250), nullable=False)
    diameter = Column(String(250))
    climate = Column(String(250))
    Planets_id = Column(Integer, ForeignKey('favorites'))
    favorites = relationship ("Favorites", back_populates =  "planets")

class Characters(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    homeworld = Column(String(250))
    birth_year = Column(String(250), nullable=False)
    characters_id = Column(Integer, ForeignKey('favorites'))
    favorites = relationship ("Favorites", back_populates =  "characters")

class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    Spaceships_id = relationship("Spaceships", back_populates="favorites")
    Spaceships = relationship( "Spaceships", back_populates="favorites")

    Planets_id = Column(ForeignKey("planets.id"))
    Planets = relationship( "Planets", back_populates="favorites")

    Characters_id = Column(ForeignKey("characters.id"))
    Characters = relationship( "Characters", back_populates="favorites")

    Favorites_id = Column(ForeignKey("user.id"))
    Favorites = relationship( "user", back_populates="favorites")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
