import uuid
from datetime import datetime


class BaseModel:
	def __init__(self, *args, **kwargs):
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def save(self):
		"""
		Update the public instance attribute 'updated_at' with the current datetime.
		"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""
		Return a dictionary containing all keys/values of the instance's __dict__.

		Returns:
			dict: A dictionary representation of the instance.
		"""
		instance_dict = self.__dict__.copy()
		instance_dict['__class__'] = self.__class__.__name__
		instance_dict['created_at'] = self.created_at.isoformat()
		instance_dict['updated_at'] = self.updated_at.isoformat()

		return instance_dict

	def __str__(self):
		"""
		Return a string representation of the object.
		"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

