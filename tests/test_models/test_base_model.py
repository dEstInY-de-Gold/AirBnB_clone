#!/usr/bin/env python3
"""Test suite for BaseModel module
"""

from models.base_model import BaseModel
import unittest
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """creating test cases for BaseModel
    """

    def setUp(self):
        """setup for the tests
        """

        self.bm = BaseModel()

    def tearDown(self):
        """teardown method
        """

        del self.bm

    def test_id(self):
        """testing id
        """

        self.assertTrue(uuid.UUID(self.bm.id))
        self.assertEqual(str, type(self.bm.id))

    def test_created_at(self):
        """testing created_at
        """

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(now, self.bm.created_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertIsInstance(self.bm.created_at, datetime)

    def test_updated_at(self):
        """testing updated_at
        """

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(now, self.bm.updated_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_str_format(self):
        """testing str return format
        """

        expected = f"[BaseModel] ({self.bm.id}) {self.bm.__dict__}"
        self.assertEqual(str(self.bm), expected)

    def test_str_update(self):
        """testing if str works after updating the instance
        """

        self.bm.name = "myname"
        expected = f"[BaseModel] ({self.bm.id}) {self.bm.__dict__}"
        self.assertEqual(str(self.bm), expected)

    def test_str_save(self):
        """checking if str updates after calling save method
        """

        self.bm.save()
        expected = f"[BaseModel] ({self.bm.id}) {self.bm.__dict__}"
        self.assertEqual(str(self.bm), expected)

    def test_save(self):
        """testing if save method updates the attributes
        """

        self.bm.save()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(now, self.bm.updated_at.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_to_dict_format(self):
        """checking the return of to_dict method
        """

        my_dict = self.bm.to_dict()
        self.assertIn("id", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("__class__", my_dict)

    def test_to_dict_attribtutes(self):
        """testing for validity of to_dict attrs
        """

        my_dict = self.bm.to_dict()
        self.assertEqual(my_dict["id"], self.bm.id)
        self.assertEqual(my_dict["created_at"], self.bm.created_at.isoformat())
        self.assertEqual(my_dict["updated_at"], self.bm.updated_at.isoformat())
        self.assertEqual(my_dict["__class__"], "BaseModel")

    def test_to_dict_update(self):
        """testing the validity of dict after upadting
        """

        self.bm.name = "test_name"
        my_dict = self.bm.to_dict()
        self.assertEqual(my_dict["name"], "test_name")

    def test_save_update_to_dict(self):
        """testing the validity of to_dict after calling save
        method
        """
        self.bm.save()
        my_dict = self.bm.to_dict()
        self.assertEqual(my_dict["updated_at"], self.bm.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
