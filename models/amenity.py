#!/usr/bin/python3
"""
Module: amenity.py

Public class:
	Amenity - a class that inherits from BaseModel and defines attributes for
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
	"""A class that inherits from BaseModel and defines attributes for
	Amenity objects.
	"""
	name = ""
