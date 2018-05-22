"""
Validate the kbase.yaml configuration data.

Configuration is set in a YAML file but converted to a python dict before getting passed here.
"""

import subprocess
from cerberus import Validator

from .exceptions import ConfigInvalid

def validate_yaml(config):
    """ Validate the kbase.yaml config """
    validator = Validator(main_schema)
    validator.validate(config)
    if validator.errors:
        raise ConfigInvalid(config, None, validator.errors)


# Cerberus schemas for the configuration file (kbase.yaml)
# --------------------------------------------------------

# Schema for an input to a direct or narrative method
method_input_schema = {
    'type': {
        'required': True,
        'type': 'string',
        'minlength': 1
    },
    'optional': {
        'type': 'boolean'
    },
    'label': {
        'required': True,
        'type': 'string',
        'minlength': 1
    }
}

# Schema for a narrative or direct method
method_schema = {
    'input': {
        'type': 'dict',
        'required': True,
        'allow_unknown': True,
        'valueschema': {
            'type': 'dict',
            'schema': method_input_schema
        }
    }
}

module_schema = {
    'name': {
        'required': True,
        'type': 'string',
        'minlength': 1
        },
    'description': {
        'required': True,
        'type': 'string',
        'minlength': 1
        },
    'version': {
        'required': True,
        'type': 'string',
        'regex': '^([0-9]+)\.([0-9]+)\.([0-9]+)$',
        'minlength': 1
        },
    'authors': {
        'type': 'list',
        'minlength': 1,
        'schema': {
            'type': 'string'
            }
        }
}

# Top-level schema for kbase.yaml
main_schema = {
    'module': {
        'required': True,
        'type': 'dict',
        'schema': module_schema
    },
    'narrative_methods': {
        'type': 'dict',
        'nullable': True,
        'allow_unknown': True,
        'valueschema': {
            'type': 'dict',
            'schema': method_schema
        }
    },
    'direct_methods': {
        'type': 'dict',
        'nullable': True,
        'allow_unknown': True,
        'valueschema': {
            'type': 'dict',
            'schema': method_schema
        }
    }
}
