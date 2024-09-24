from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql


pymysql.install_as_MySQLdb()

DATABASE_URL = "mysql+pymysql://root:Okenna1996.#@localhost/ross_b"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

session = Session()
