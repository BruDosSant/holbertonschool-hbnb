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

def test_create_amenity(self):
        """Test that an amenity can be created"""
        amenity_data = {"name": "WiFi"}  # Example amenity
        
        amenity = self.facade.create_amenity(amenity_data)  # Create an amenity
        
        self.assertIsNotNone(amenity)  # Verify it was created successfully
        self.assertEqual(amenity.name, "WiFi")  # Verify the name is correct

    def test_create_amenity_with_empty_name(self):
        """Test that an amenity cannot be created with an empty name"""
        amenity_data = {"name": ""}  # Example amenity
    
        with self.assertRaises(ValueError):  # Expect an exception to be raised
            self.facade.create_amenity(amenity_data)

    def test_create_amenity_with_long_name(self):
        """Test that an amenity cannot be created with a name longer than 50 characters"""
        amenity_data = {"name": "dasjdkasdkasjdkasjdkasdjaslkdjaskdjasdklasjdassadasdasdsadasd"}  # Example amenity
    
        with self.assertRaises(ValueError):  # Expect an exception to be raised
            self.facade.create_amenity(amenity_data)