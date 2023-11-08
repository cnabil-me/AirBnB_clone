#!/usr/bin/python3
"""
Module: state.py

Public class:
	State - a class that inherits from BaseModel and defines attributes for a
	state in the application
"""
from models.base_model import BaseModel


class State(BaseModel):
	"""
	State class that inherits from BaseModel
	representing a state in the application.
	Attributes:
		name
	"""
	name = ""
