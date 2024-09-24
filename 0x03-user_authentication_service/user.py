#!/usr/bin/env python3
"""Class User for ORM"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# Define the User model class
class User(Base):
    # Specify the name of the table in the database
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)  # primary key
    email = Column(String(250), nullable=False)  # string for email
    hashed_password = Column(String(250), nullable=False)  # string
    session_id = Column(String(250))  # string for session ID
    reset_token = Column(String(250))  # string for reset token
