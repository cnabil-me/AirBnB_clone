#!usr/bin/python3
"""
Module: user.py
Public class:
User - a class that inherits from BaseModel and defines attributes for
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel represents a user for the
    application
    Attributes: email password first_name last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
