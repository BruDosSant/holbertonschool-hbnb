#!/usr/bin/python3
"""Base Class"""


import uuid
from datetime import datetime
from flask_swagger_ui import get_swaggerui_blueprint


class BaseModel:
    """Class Base, from which all other classes inherits"""
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()