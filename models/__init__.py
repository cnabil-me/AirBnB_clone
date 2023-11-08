#!/usr/bin/python3
"""
Module: Models contains the classes used by the console
classes:
    BaseModel - defines all common attributes/methods for other classes
    User - defines attributes for User objects
    State - defines attributes for State objects
    City - defines attributes for City objects
    Amenity - defines attributes for Amenity objects
    Place - defines attributes for Place objects
    Review - defines attributes for Review objects

"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
