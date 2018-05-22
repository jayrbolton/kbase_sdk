import os
import unittest
import shutil
import tempfile

import kbase_sdk
from kbase_sdk.config_validation.validate_paths import validate_paths
from kbase_sdk.config_validation.exceptions import MissingPath
from test.test_utils.initializers import init_temp_app


class TestValidatePaths(unittest.TestCase):

    def test_valid_paths(self):
        """ Test an app that has all valid paths """
        base_dir = os.path.dirname(__file__)
        app_dir = os.path.join(base_dir, '..', 'test_app')
        context = kbase_sdk.init_context(app_dir)
        validate_paths(context['paths'])  # Does not raise

    def test_invalid_paths(self):
        """ Iteratively rename some paths in context['paths'] and check for the proper MissingPath """
        app_dir = init_temp_app()
        context = kbase_sdk.init_context(app_dir)
        path_names = [
            'config',
            'main_module',
            'test_main_module'
        ]
        for name in path_names:
            path = context['paths'][name]
            shutil.move(path, path + '.bak')
            with self.assertRaises(MissingPath) as err:
                validate_paths(context['paths'])
            self.assertEqual(err.exception.path, path)
            self.assertEqual(err.exception.name, name)
            shutil.move(path + '.bak', path)
