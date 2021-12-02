""" -------------------------------------------------------------------------------------------------------------------
* PROJECT:  DPG-Bot
* PACKAGE:  DATABASE
* FILE:     models.py
* CONTENT:  Create models for the pydantic database work
* STATIC:
---------------------------------------------------------------------------------------------------------------------"""
from sqlalchemy import Column, String, Float

from database.database import Base


class DPG_API_NEW(Base):
    """
    Table DPG_API_NEW;
    """
    __tablename__ = 'dpg_api_new'
    Command = Column(String, primary_key=True)
    Message = Column(String)


class DPG_DOCS(Base):
    """
    Table DPG_DOCS;
    """
    __tablename__ = 'dpg_docs'
    Command = Column(String, primary_key=True)
    Message = Column(String)
