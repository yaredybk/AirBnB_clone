#!/usr/bin/python3
# unit tests for basemodel

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel_init(unittest.TestCase):
    """unit tests for initialization of BaseModel"""

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_unique_id(self):
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

    def test_from_kwargs(self):
        d1 = {
                'id': '56dfb799-bd1e-4173-a6f5-d8664779db91',
                'created_at': '2024-03-09T22:06:44.139049',
                'updated_at': '2024-03-09T22:06:44.233277',
                '__class__': 'WrongBaseModel'
                }
        m1 = BaseModel(**d1)
        m2 = BaseModel(**d1)
        m3 = BaseModel(**{})
        self.assertEqual(d1["id"], m1.id)
        self.assertEqual(m2.id, m1.id)
        self.assertEqual(datetime, type(m1.created_at))
        self.assertEqual(datetime, type(m1.updated_at))
        self.assertNotEqual(m1.__class__, "WrongBaseModel")
        self.assertTrue(hasattr(m3, "id"))

class TestBaseModel_methods(unittest.TestCase):
    """unit tests for base model methods"""

    base1 = BaseModel()

    def test_save(self):
        tmp = self.base1.updated_at
        self.base1.save()
        self.assertNotEqual(tmp, self.base1.updated_at)

    def test_to_dict(self):
        tmp = self.base1.to_dict()
        self.assertTrue(hasattr(tmp, "__class__"))
        self.assertEqual("BaseModel", tmp["__class__"])
        self.assertEqual(type(tmp["created_at"]),str)
