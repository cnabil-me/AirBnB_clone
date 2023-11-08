#!/usr/bin/python3
"""Module: city.py

Public class:
	City - a class that inherits from BaseModel and defines attributes for
	City objects.

"""
from models.base_model import BaseModel


class City(BaseModel):
	"""A class that inherits from BaseModel and defines attributes for
	City objects.
	"""
	name = ""
	state_id = ""
