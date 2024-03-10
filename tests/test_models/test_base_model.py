#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, old_updated_at)

    def test_to_dict(self):
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in base_model_dict)
        self.assertTrue('created_at' in base_model_dict)
        self.assertTrue('updated_at' in base_model_dict)

    def test_str(self):
        expected_str = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)


if __name__ == '__main__':
    unittest.main()
