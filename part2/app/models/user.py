#!/usr/bin/python3
"""Class User"""

import uuid
from app.models.base import BaseModel
from email_validator import validate_email, EmailNotValidError
from flask import current_app



class User(BaseModel):
    """Class User, inherits from BaseModel"""
    
    def __init__(self, first_name: str, last_name: str, email: str, password: str, is_admin: bool = False):
        super().__init__()
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hash_password(password)
        self.is_admin = is_admin

    
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value or len(value) > 50:
            raise ValueError("First name is required and cannot exceed 50 characters")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if not value or len(value) > 50:
            raise ValueError("Last name is required and cannot exceed 50 characters")
        self._last_name = value
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        try:
            email_info = validate_email(value, check_deliverability=False)  
            self._email = email_info.normalized
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email: {e}")
        
    def hash_password(self, password):
        from app import bcrypt
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        from app import bcrypt
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
