#!/usr/bin/python3
"""
Module: review.py

Public class:
    Review - a class that inherits from BaseModel and defines attributes for
    Review objects.

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel
    representing a review of a place/house.
    Attributes:
        text
        user_id
        place_id
    """
    text = ""
    user_id = ""
    place_id = ""
