#!/usr/bin/python3
"""
	Module: file_storage.py
	Description: Defines the FileStorage class.

	Classes:
		FileStorage

"""
import json
import os

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
	"""
	A class that serializes instances to a JSON file and deserializes JSON file
	to instances.

	__file_path: string - path to the JSON file (ex: file.json)
	__objects: dictionary - empty but will store all objects by <class name>.id

	"""
	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""
		Retries the dictionary __objects
		:self: the object itself
		:return:  the dictionary __objects
		"""
		return FileStorage.__objects

	def new(self, obj):
		"""
		sets in __objects the obj with key <obj class name>.id
		:self: the object itself
		:obj: the object to set in __objects
		:return: void
		"""
		key = "{}.{}".format(type(obj).__name__, obj.id)
		FileStorage.__objects[key] = obj

	def save(self):
		"""
		Saves the dictionary __objects to the JSON file
		:self: the object itself
		:return: void
		"""
		with open(FileStorage.__file_path, 'w') as f:
			json.dump(
				{k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

	def reload(self):
		"""
		Deserializes the JSON file to __objects (only if the JSON file
		exists ; otherwise, do nothing. If the file not exist, no
		exception should be raised)
		:self: the object itself
		:return: void
		"""
		current_classes = {
			'BaseModel': BaseModel, 'User': User,
			'Amenity': Amenity, 'City': City, 'State': State,
			'Place': Place, 'Review': Review
		}

		if not os.path.exists(FileStorage.__file_path):
			return

		with open(FileStorage.__file_path, 'r') as f:
			deserialized = None

			try:
				deserialized = json.load(f)
			except json.JSONDecodeError:
				pass

			if deserialized is None:
				return

			FileStorage.__objects = {
				k: current_classes[k.split('.')[0]](**v)
				for k, v in deserialized.items()}
