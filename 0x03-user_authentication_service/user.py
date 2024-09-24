#!/usr/bin/env python3
"""Class User for ORM"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# 1. Define the User model class
class User(Base):
    # 2. Specify the name of the table in the database
    __tablename__ = 'users'

    # 3. Define the columns in the users table
    id = Column(Integer, primary_key=True)  # primary key
    email = Column(String(250), nullable=False)  # string for email
    hashed_password = Column(String(250), nullable=False)  # string
    session_id = Column(String(250), nullable=True)  # string for session ID
    reset_token = Column(String(250), nullable=True)  # string for reset token
