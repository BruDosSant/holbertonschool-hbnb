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

    def test_get_all(self):
            """Test that all elements can be retrieved"""
            
            users = self.facade.get_all()  # Get all users
            amenities = self.facade.get_all_amenities()  # Get all amenities
            places = self.facade.get_all_places()  # Get all places
            
            # Verify that each is a list (even if empty)
            self.assertIsInstance(users, list)
            self.assertIsInstance(amenities, list)
            self.assertIsInstance(places, list)