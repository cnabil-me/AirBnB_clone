#!/usr/bin/python3
"""This module defines a base class for all models in our AirBnB clone"""

import uuid
from datetime import datetime


class BaseModel:
	"""A base class for all AirBnB models"""

	def __init__(self, *args, **kwargs):
		"""
		Instantiates a new model
		Args:
			*args: a list of arguments
			**kwargs: A dictionary of arguments and values for the
			model
		id: uuid when an instance is created.
		created_at: timestamp of the creation of an instance
		updated_at: timestamp of the last update of an instance
		"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()
		if kwargs:
			for key, value in kwargs.items():
				if key == "__class__":
					continue
				elif key == "created_at" or key == "updated_at":
					value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
				setattr(self, key, value)

	def __str__(self):
		"""Returns a string representation of the instance"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		"""Updates updated_at with the current datetime"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""Returns a dictionary containing all keys&values of __dict__ instance"""
		instance_dict = self.__dict__.copy()
		instance_dict["__class__"] = self.__class__.__name__
		instance_dict["created_at"] = self.created_at.isoformat()
		instance_dict["updated_at"] = self.updated_at.isoformat()
		return instance_dict
