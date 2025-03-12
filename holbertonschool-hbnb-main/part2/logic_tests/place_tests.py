#!/usr/bin/python3
"""Tests for the Place endpoints"""

import unittest
from app import create_app
from app.services.facade import HBnBFacade
from app.models.user import User
from app.models.place import Place

class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.facade = HBnBFacade()
        self.user = self.facade.create_user({
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        })

    def test_create_place(self):
        """Test that a place can be created"""
        place_data = {
            "title": "Departamento pequeño",
            "description": "Un pequeño departamento en el centro de la ciudad",
            "price": 50,
            "latitude": 40.0,
            "longitude": -74.0,
            "owner_id": self.user.id
        }
        response = self.client.post('/api/v1/places/', json=place_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_create_place_with_invalid_coordinates(self):
        """Test that a place cannot be created with invalid coordinates"""
        place_data = {
            "title": "Departamento pequeño",
            "description": "Un pequeño departamento en el centro de la ciudad",
            "price": 50,
            "latitude": 200.0,  # Invalid latitude
            "longitude": -200.0,  # Invalid longitude
            "owner_id": self.user.id
        }
        response = self.client.post('/api/v1/places/', json=place_data)
        self.assertEqual(response.status_code, 400)

    def test_create_place_with_empty_user_data(self):
        """Test that a place cannot be created with empty user data"""
        user_data = {
            "first_name": "",
            "last_name": "",
            "email": ""
        }
        response = self.client.post('/api/v1/users/', json=user_data)
        self.assertEqual(response.status_code, 400)

    def test_create_place_with_empty_owner(self):
        """Test that a place cannot be created with an empty owner field"""
        place_data = {
            "title": "Departamento pequeño",
            "description": "Un pequeño departamento en el centro de la ciudad",
            "price": 50,
            "latitude": 40.0,
            "longitude": -74.0,
            "owner_id": None  # Empty owner
        }
        response = self.client.post('/api/v1/places/', json=place_data)
        self.assertEqual(response.status_code, 400)

    def test_create_place_with_empty_first_name(self):
        """Test that a place cannot be created with an empty first name"""
        user_data = {
            "first_name": "",
            "last_name": "Rios",
            "email": "lu.rios@example.com"
        }
        response = self.client.post('/api/v1/users/', json=user_data)
        self.assertEqual(response.status_code, 400)

    def test_create_place_with_empty_last_name(self):
        """Test that a place cannot be created with an empty last name"""
        user_data = {
            "first_name": "Lu",
            "last_name": "",
            "email": "lu.rios@example.com"
        }
        response = self.client.post('/api/v1/users/', json=user_data)
        self.assertEqual(response.status_code, 400)

    def test_create_place_with_empty_email(self):
        """Test that a place cannot be created with an empty email"""
        user_data = {
            "first_name": "Lu",
            "last_name": "Rios",
            "email": ""
        }
        response = self.client.post('/api/v1/users/', json=user_data)
        self.assertEqual(response.status_code, 400)

    def test_create_place_with_empty_title(self):
        """Test that a place cannot be created with an empty title"""
        place_data = {
            "title": "",  # Empty title
            "description": "Un pequeño departamento en el centro de la ciudad",
            "price": 50,
            "latitude": 40.0,
            "longitude": -74.0,
            "owner_id": self.user.id
        }
        response = self.client.post('/api/v1/places/', json=place_data)
        self.assertEqual(response.status_code, 400)

    def test_create_place_with_empty_description(self):
        """Test that a place cannot be created with an empty description"""
        place_data = {
            "title": "Departamento pequeño",
            "description": "",  # Empty description
            "price": 50,
            "latitude": 40.0,
            "longitude": -74.0,
            "owner_id": self.user.id
        }
        response = self.client.post('/api/v1/places/', json=place_data)
        self.assertEqual(response.status_code, 400)

    def test_create_place_with_empty_price(self):
        """Test that a place cannot be created with an empty price"""
        place_data = {
            "title": "Departamento pequeño",
            "description": "Un pequeño departamento en el centro de la ciudad",
            "price": None,  # Empty price
            "latitude": 40.0,
            "longitude": -74.0,
            "owner_id": self.user.id
        }
        response = self.client.post('/api/v1/places/', json=place_data)
        self.assertEqual(response.status_code, 400)

    def test_create_place_with_empty_latitude(self):
        """Test that a place cannot be created with an empty latitude"""
        place_data = {
            "title": "Departamento pequeño",
            "description": "Un pequeño departamento en el centro de la ciudad",
            "price": 50,
            "latitude": None,  # Empty latitude
            "longitude": -74.0,
            "owner_id": self.user.id
        }
        response = self.client.post('/api/v1/places/', json=place_data)
        self.assertEqual(response.status_code, 400)

    def test_create_place_with_empty_longitude(self):
        """Test that a place cannot be created with an empty longitude"""
        place_data = {
            "title": "Departamento pequeño",
            "description": "Un pequeño departamento en el centro de la ciudad",
            "price": 50,
            "latitude": 40.0,
            "longitude": None,  # Empty longitude
            "owner_id": self.user.id
        }
        response = self.client.post('/api/v1/places/', json=place_data)
        self.assertEqual(response.status_code, 400)

# This runs the tests when the file is executed
if __name__ == '__main__':
    unittest.main()