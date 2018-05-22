import os
import unittest

import kbase_sdk.param_validation.exceptions as exceptions
from test.test_app.src.main import my_method

base_dir = os.path.dirname(__file__)


class TestValidateParams(unittest.TestCase):

    def setUp(self):
        os.environ['KBASE_ROOT'] = os.path.join(base_dir, 'test_app')

    def test_valid_params(self):
        # 'y' is an optional field
        self.assertTrue(my_method({'x': 100}))
        self.assertTrue(my_method({'x': 100, 'y': 'str'}))

    def test_missing_fields(self):
        with self.assertRaises(exceptions.InvalidParams) as err:
            my_method({})
        self.assertEqual(err.exception.params, {})
        self.assertEqual(err.exception.errors, {'x': ['required field']})

    def test_invalid_type(self):
        with self.assertRaises(exceptions.InvalidParams) as err:
            my_method({'x': 'hi', 'y': 1})
        self.assertEqual(err.exception.params, {'x': 'hi', 'y': 1})
        self.assertEqual(err.exception.errors, {'x': ['must be of integer type'], 'y': ['must be of string type']})
