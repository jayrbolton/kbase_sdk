import os
import unittest
import shutil
import tempfile

from kbase_sdk.config_validation.validate_paths import validate_paths
from kbase_sdk.config_validation.exceptions import MissingPathException
from .test_utils.initializers import init_temp_app


class TestMain(unittest.TestCase):

    def setUp(self):
        self.test_app_dir = os.path.join(os.path.dirname(__file__), '..', 'test_app')
        # Initialize a temporary parent directory
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove all temp files
        shutil.rmtree(self.temp_dir)

    def test_valid_paths(self):
        """ Test an app that has all valid paths """
        context = init_temp_app(self.temp_dir)
        validate_paths(context)  # Does not raise

    def test_invalid_paths(self):
        """ Iteratively rename some paths in context['paths'] and check for the proper MissingPathException """
        context = self.init_temp_app()
        path_names = [
            'config',
            'main_module',
            'test_main_module'
        ]
        context = self.init_temp_app()
        for name in path_names:
            path = context['paths'][name]
            shutil.move(path, path + '.bak')
            with self.assertRaises(MissingPathException) as err:
                validate_paths(context)
            self.assertEqual(err.exception.path, path)
            self.assertEqual(err.exception.name, name)
            shutil.move(path + '.bak', path)
