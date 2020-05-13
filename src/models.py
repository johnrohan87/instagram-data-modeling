import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = relationship('address')
    posting = relationship('posting')
    picture = relationship('picture')


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Posting(Base):
    __tablename__ = 'posting'
    id = Column(Integer, primary_key=True)
    post_content = Column(String(250))
    post_comment = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))
    picture = Column(Integer, ForeignKey('picture.id'))

class Picture(Base):
    __tablename__ = 'picture'
    id = Column(Integer, primary_key=True)
    post_picture = Column(String(250))
    person_id = Column(Integer, ForeignKey('person.id'))
    posting_id = Column(Integer, ForeignKey('posting.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
