""" -------------------------------------------------------------------------------------------------------------------
* PROJECT:  DPG-Bot
* PACKAGE:  DATABASE
* FILE:     database.py
* CONTENT:  Create visible SQLITE3 Database to store changes
* STATIC:
---------------------------------------------------------------------------------------------------------------------"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./DPGDB.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SessionThread = sessionmaker()
SessionThread.configure(bind=engine)

Base = declarative_base()



