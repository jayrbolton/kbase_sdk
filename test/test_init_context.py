import os
import unittest
import shutil

import kbase_sdk
from test.test_utils.initializers import init_temp_app
from kbase_sdk.config_validation.exceptions import MissingPath


class TestInitContext(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.base_dir = os.path.dirname(__file__)
        self.test_app_dir = init_temp_app()

    def tearDown(self):
        shutil.rmtree(self.test_app_dir)

    def test_valid_app(self):
        """ Test the successful case and all keys in the context dict """
        # Initialize the app using os.getcwd()
        os.chdir(self.test_app_dir)
        kbase_sdk.init_context.cache_clear()
        context = kbase_sdk.init_context()
        self.assertEqual(context, {
            'paths': {
                'root': self.test_app_dir,
                'config': os.path.join(self.test_app_dir, 'kbase.yaml'),
                'main_module': os.path.join(self.test_app_dir, 'src', 'main.py'),
                'src_dir': os.path.join(self.test_app_dir, 'src'),
                'test_dir': os.path.join(self.test_app_dir, 'test'),
                'test_main_module': os.path.join(self.test_app_dir, 'test', 'test_main.py')
            },
            'config': {
                'module': {
                    'name': 'test_module',
                    'description': 'xyz',
                    'version': '0.0.1',
                    'authors': ['xyz']
                },
                'narrative_methods': {
                    'my_method': {
                        'input': {
                            'x': {
                                'label': 'label',
                                'type': 'integer'
                            },
                            'y': {
                                'label': 'label',
                                'type': 'string',
                                'optional': True
                            }
                        }
                    }
                },
            },
            'docker_image_name': 'kbase-apps/test_module',
            'username': 'jayrbolton',
            'token': 'xyz'
        })

    def test_invalid_app(self):
        """ Test that init_context raises errors with validate_paths """
        kbase_sdk.init_context.cache_clear()
        config_path = os.path.join(self.test_app_dir, 'kbase.yaml')
        # Move kbase.yaml to kbase.yaml.bak
        shutil.move(config_path, config_path + '.bak')
        with self.assertRaises(MissingPath) as err:
            kbase_sdk.init_context(self.test_app_dir)
        self.assertEqual(err.exception.path, config_path)
        self.assertEqual(err.exception.name, 'config')
        shutil.move(config_path + '.bak', config_path)

    def test_cache_results(self):
        """ Test that the results cache properly by moving kbase.yaml """
        kbase_sdk.init_context.cache_clear()
        config_path = os.path.join(self.test_app_dir, 'kbase.yaml')
        # Move kbase.yaml to kbase.yaml.bak
        context1 = kbase_sdk.init_context(self.test_app_dir)
        shutil.move(config_path, config_path + '.bak')
        context2 = kbase_sdk.init_context(self.test_app_dir)
        # If it's not caching, then MissingPath would be raised
        self.assertEqual(context1, context2)
        shutil.move(config_path + '.bak', config_path)
