#!/usr/bin/python3
"""Unit tests for the FileStorage class"""
import unittest
import os
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.test_obj = BaseModel()
        self.storage = storage

    def tearDown(self):
        """Remove test environment"""
        del self.test_obj
        del self.storage

    def test_all(self):
        """Test the all() method"""
        new_obj = BaseModel()  # Create a new object
        self.storage.new(new_obj)
        all_objs = self.storage.all()
        self.assertIn(new_obj.__class__.__name__ + '.' + new_obj.id, all_objs)

    def test_new(self):
        """Test the new() method"""
        new_obj = BaseModel()
        self.storage.new(new_obj)
        all_objs = self.storage.all()
        self.assertIn(new_obj.__class__.__name__ + '.' + new_obj.id, all_objs)

    def test_save_reload(self):
        """Test the save() and reload() methods"""
        num_objects_before = len(self.storage.all())
        self.storage.save()
        self.storage.reload()
        num_objects_after = len(self.storage.all())
        self.assertEqual(num_objects_before, num_objects_after)

    def test_file_exists(self):
        """Test if the file exists after saving"""
        self.storage.save()
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))

    def test_reload_empty_file(self):
        """Test reloading from an empty file"""
        empty_file = 'empty.json'  # Choose a filename for an empty file
        with open(empty_file, 'w') as f:
            f.write("")  # Create an empty file
        storage._FileStorage__file_path = empty_file
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_nonexistent_file(self):
        """Test reloading from a nonexistent file"""
        nonexistent_file = 'nonexistent.json'  # Use the correct file name
        storage._FileStorage__file_path = nonexistent_file
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_invalid_json(self):
        """Test reloading from a file with invalid JSON data"""
        with open(self.storage._FileStorage__file_path, 'w') as f:
            f.write('invalid json')
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

if __name__ == '__main__':
    unittest.main()
