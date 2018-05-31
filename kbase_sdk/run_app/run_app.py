"""
A utility for running other SDK apps
"""

from cerberus import Validator
from .exceptions import InvalidRunAppParams

AUTH_URL = 'https://kbase.us/services/authorization/Sessions/Login'
HOST_URL = 'https://appdev.kbase.us'


def run_app(context, options):
    print('running an app in context', context['paths']['root'])
    print('token:', context['token'])

    schema = {
        'app': {
            'required': True,
            'type': 'string',
            'minlength': 1
        },
        'method': {
            'required': True,
            'type': 'string',
            'minlength': 1
        }
    }

    validator = Validator(schema)
    validator.validate(options)
    if validator.errors:
        raise InvalidRunAppParams(validator.errors)

    app_name = options['app']
    method_name = options['method']
    params = options.get('params', {})

    return app_name, method_name, params
