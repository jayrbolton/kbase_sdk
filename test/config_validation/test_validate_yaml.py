"""
Tests for kbase_sdk/config_validation/validate_yaml.py
"""

import os
import unittest

from kbase_sdk.config_validation.exceptions import ConfigInvalid
from kbase_sdk.init_context import load_yaml
from kbase_sdk.config_validation.validate_yaml import validate_yaml


class TestValidateYaml(unittest.TestCase):
    """
    Test cases:
    - Fully valid config
    - Missing required module or method fields
    - No unknown fields
    - Wrong field types
    - Duplicate method names
    """

    def setUp(self):
        self.base_dir = os.path.dirname(__file__)
        self.example_dir = os.path.join(self.base_dir, 'example_configs')

    def test_valid_config(self):
        """ Test a simple valid config with module info """
        path = os.path.join(self.example_dir, 'valid_basic.yaml')
        yaml = load_yaml(path)
        result = validate_yaml(yaml)
        self.assertEqual(result, None)

    def test_missing_module_keys(self):
        """ Test a simple valid config with module info """
        path = os.path.join(self.example_dir, 'valid_basic.yaml')
        config = load_yaml(path)
        keys = ['name', 'description', 'version', 'authors']
        for key in keys:
            val = config['module'][key]
            del config['module'][key]
            with self.assertRaises(ConfigInvalid) as err:
                validate_yaml(config)
            self.assertEqual(err.exception.given_config, config)
            self.assertEqual(err.exception.key_errors, {'module': [{key: ['required field']}]})
            config['module'][key] = val

    @unittest.skip('TODO')
    def test_invalid_semver(self):
        """ Test validity checker for the semantic version under module.version """
        pass

    @unittest.skip('TODO')
    def test_method_schemas(self):
        """
        For method schemas, test:
        - No unknown params
        - Required fields: input, type, label
        - Invalid input types
        """
        pass
