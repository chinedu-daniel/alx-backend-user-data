#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import pymysql


pymysql.install_as_MySQLdb()

DATABASE_URL = "mysql+pymysql://root:Okenna1996.#@localhost/ross_b"

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

# Declarative base class
Base = declarative_base()

# Create session
Session = sessionmaker(bind=engine)

# Create all tables in the database (ensure models are defined)
Base.metadata.create_all(engine)

# You can now use Session() to interact with the database
session = Session()
