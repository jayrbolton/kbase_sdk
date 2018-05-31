import os
import unittest
import shutil

import kbase_sdk
from kbase_sdk.run_app.exceptions import InvalidRunAppParams
from test.test_utils.initializers import init_temp_app


class TestRunApp(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.dirname(__file__)
        self.test_app_dir = init_temp_app()
        os.chdir(self.test_app_dir)
        self.context = kbase_sdk.init_context(self.test_app_dir)

    def tearDown(self):
        shutil.rmtree(self.test_app_dir)

    def test_basic_valid(self):
        result = kbase_sdk.run_app(self.context, {
            'app': 'App',
            'method': 'method'
        })
        print(result)

    def test_requires_method_name(self):
        with self.assertRaises(InvalidRunAppParams) as err:
            kbase_sdk.run_app(self.context, {'app': 'x'})
        self.assertEqual(err.exception.errors, {'method': ['required field']})

    def test_requires_app_name(self):
        with self.assertRaises(InvalidRunAppParams) as err:
            kbase_sdk.run_app(self.context, {'method': 'x'})
        self.assertEqual(err.exception.errors, {'app': ['required field']})
