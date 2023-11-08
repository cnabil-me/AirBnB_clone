#!/usr/bin/python3
"""
Module: base_model.py
"""
import uuid
from datetime import datetime

import models


class BaseModel:
    """
    Base class for other classes to be used for the duration
    of the AirBnB project
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the instance of the class
        :self: the object itself
        :param args: unused
        :param kwargs: dictionary of key/value pairs
        :return: void
        """

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the instance
        :self: the object itself
        :return: string representation of the instance
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        update date and time for the current instance and saves
        :self: the object itself
        :return: void
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        :self: the object itself
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dictionary_object = {**self.__dict__, '__class__': type(self).__name__}
        dictionary_object['created_at'] = dictionary_object['created_at'].isoformat()
        dictionary_object['updated_at'] = dictionary_object['updated_at'].isoformat()

        return dictionary_object
