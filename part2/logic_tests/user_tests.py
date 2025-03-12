#!/usr/bin/python3
"""Tests for the HBnB Facade"""

import unittest  # Import the unittest library
from app import create_app  # Import the Flask app
from app.services.facade import HBnBFacade  # Import the Facade
import app.models

class TestHBnBFacade(unittest.TestCase):  # Create our test class
    test_user = 0

    def setUp(self):  # This runs BEFORE each test
        self.app = create_app()  # Create the Flask app
        self.client = self.app.test_client()  # Client to make requests
        self.facade = HBnBFacade()  # Create the Facade that handles data

    def test_create_user(self):  
        """Test that a user can be created"""
        user_data = {
            "first_name": "Jhon", 
            "last_name": "doe", 
            "email": "jhon.doe@example.com"
        }
        
        user = self.facade.create_user(user_data)  # Create a user
        test_user = user

        self.assertIsNotNone(user)  
        self.assertEqual(user.first_name, "Jhon")

    def test_create_user_with_empty_first_name(self):  
        """Test that a user cannot be created with an empty first name"""
        user_data = {
            "first_name": "", 
            "last_name": "Doe", 
            "email": "juan.doe@example.com"
        }
    
        with self.assertRaises(ValueError):  # Expect an exception to be raised
            self.facade.create_user(user_data)
    
    def test_create_user_with_empty_last_name(self):  
        """Test that a user cannot be created with an empty last name"""
        user_data = {
            "first_name": "Jhon", 
            "last_name": "", 
            "email": "jhon.doe@example.com"
        }

        with self.assertRaises(ValueError):  # Expect an exception to be raised
            self.facade.create_user(user_data)

    def test_create_user_with_empty_email(self):  
        """Test that a user cannot be created with an empty email"""
        user_data = {
            "first_name": "jhon", 
            "last_name": "doe", 
            "email": ""
        }

        with self.assertRaises(ValueError):  # Expect an exception to be raised
            self.facade.create_user(user_data)

    def test_create_user_with_invalid_email(self):  
        """Test that a user cannot be created with an invalid email"""
        user_data = {
            "first_name": "jhon", 
            "last_name": "doe", 
            "email": "jhon.doeexample.com"
        }

        with self.assertRaises(ValueError):  # Expect an exception to be raised
            self.facade.create_user(user_data)

    def test_create_user_without_dot_com(self):  
        """Test that a user cannot be created without .com in email"""
        user_data = {
            "first_name": "jhon", 
            "last_name": "doe", 
            "email": "jhon.doeexample"
        }

        with self.assertRaises(ValueError):  # Expect an exception to be raised
            self.facade.create_user(user_data)

    def test_create_user_with_empty_fields(self):  
        """Test that a user cannot be created with empty fields"""
        user_data = {
            "first_name": "", 
            "last_name": "", 
            "email": ""
        }

        with self.assertRaises(ValueError):  # Expect an exception to be raised
            self.facade.create_user(user_data)
    
    def test_create_user_with_numeric_fields(self):  
        """Test that a user cannot be created with numeric fields"""
        user_data = {
            "first_name": "123434234", 
            "last_name": "3232323", 
            "email": "7855665465456"
        }

        with self.assertRaises(ValueError):  # Expect an exception to be raised
            self.facade.create_user(user_data)

    def test_create_user_with_invalid_email_format(self):  
        """Test that a user cannot be created with an invalid email format"""
        user_data = {
            "first_name": "1234", 
            "last_name": "doe", 
            "email": "jhon.doeexample"
        }

        with self.assertRaises(ValueError):  # Expect an exception to be raised
            self.facade.create_user(user_data)

    def test_create_user_with_numeric_last_name(self):  
        """Test that a user cannot be created with a numeric last name"""
        user_data = {
            "first_name": "jhon", 
            "last_name": "12344", 
            "email": "jhon.doeexample"
        }

        with self.assertRaises(ValueError):  # Expect an exception to be raised
            self.facade.create_user(user_data)

    def test_create_user_with_invalid_email_without_dot_com(self):  
        """Test that a user cannot be created with an invalid email without .com"""
        user_data = {
            "first_name": "Jhon", 
            "last_name": "doe", 
            "email": "1515654"
        }

        with self.assertRaises(ValueError):  # Expect an exception to be raised
            self.facade.create_user(user_data)
    

    ef test_get_by_id(self):
        """Test that a user can be retrieved by ID"""
        
        # Create a test user
        user_data = {
            "first_name": "Test", 
            "last_name": "User", 
            "email": "test@example.com"
        }
        user = self.facade.create_user(user_data)
        
        # Retrieve by ID
        fetched_user = self.facade.get_user(user.id)
        
        # Verify it's the same user
        self.assertIsNotNone(fetched_user)
        self.assertEqual(fetched_user.email, "test@example.com")

    def test_update_user(self):
        """Test that a user can be updated"""
        
        # Create a user
        user_data = {
            "first_name": "Luis", 
            "last_name": "Gómez", 
            "email": "luis.gomez@example.com"
        }
        user = self.facade.create_user(user_data)
        
        # Update the first name
        updated_user = self.facade.update_user(user.id, {"first_name": "Carlos"})
        
        # Verify the name changed
        self.assertEqual(updated_user.first_name, "Carlos")