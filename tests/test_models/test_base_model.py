#!/usr/bin/python3
# unit tests for basemodel

import unittest
from models import BaseModel
import datetime


class TestBaseModel_init(unittest.TestCase):
    """unit tests for initialization of BaseModel"""

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_uniqueid(self):
        self.assertNotEqual(BaseModel().id, BaseModel().id)

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_unique_created_at(self):
        self.assertNotEqual(BaseModel().created_at, BaseModel().created_at)

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_dict(self):
        tmp = BaseModel()
        tmp.id = "123"
        self.assertIn("[BaseModel] (123) ", str(tmp))


class TestBaseModel_methods(unittest.TestCase):
    """unit tests for base model methods"""

    base1 = BaseModel()

    def test_save(self):
        self.assertNotEqual(base1.updated_at, base1.save().updated_at)

    def test_to_dict(self):
        tmp = base1.to_dict()

        self.assertEqual("BaseModel", tmp.__class__)
        self.assertEqual(datetime.isoformat(base1.created_at), tmp.created_at)
