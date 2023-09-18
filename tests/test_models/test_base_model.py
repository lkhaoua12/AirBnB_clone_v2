#!/usr/bin/python3
"""Unit tests for BaseModel class"""

from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        """Test the attributes of the BaseModel instance"""
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_id_type(self):
        """Test the type of 'id' attribute"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at_type(self):
        """Test the type of 'created_at' attribute"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_type(self):
        """Test the type of 'updated_at' attribute"""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        """Test the __str__ method"""
        model = BaseModel()
        str_repr = str(model)
        self.assertTrue('[BaseModel]' in str_repr)
        self.assertTrue('id' in str_repr)
        self.assertTrue('created_at' in str_repr)
        self.assertTrue('updated_at' in str_repr)

    def test_save_method(self):
        """Test the save method"""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(type(model_dict['created_at']), str)
        self.assertEqual(type(model_dict['updated_at']), str)
        self.assertEqual(type(model_dict['id']), str)

if __name__ == '__main__':
    unittest.main()
