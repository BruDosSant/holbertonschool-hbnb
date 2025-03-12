#!/usr/bin/python3
"""Class Place"""

import uuid
from .base import BaseModel
from .user import User


class Place(BaseModel):
    """Class Place, inherits from BaseModel"""

    def __init__(self, title: str, price: float, latitude: float, longitude: float, owner: User, description=None, amenities=None, reviews=None, place_id=None):
        """Constructor method"""      
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = amenities or []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not value or len(value) > 100:
            raise ValueError("Title is required and cannot exceed 100 characters")
        self._title = value

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if  value is None or len(value) == 0:
            raise ValueError("Description cannot be empty")
        if len(value) > 100:
            raise ValueError("Description cannot exceed 100 caracters")
        self._description = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value is None or value < 0:
            raise ValueError("Price must be a positive number")
        self._price = value

    @property
    def latitude(self):
        return self._latitude
    
    @latitude.setter
    def latitude(self, value):
        if value is None or value < -90.0 or value > 90.0:
            raise ValueError("Must be within the range of -90.0 to 90.0.")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude
    
    @longitude.setter
    def longitude(self, value):  
        if value is None or value < -180.0 or value > 180.0:
            raise ValueError("Must be within the range of -180.0 to 180.0.")
        self._longitude = value

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):  
        if not isinstance(value, User):
            raise ValueError("Owner must be a User instance")
        self._owner = value
    
    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
