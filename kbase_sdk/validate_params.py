"""
Run-time type validation of function parameters based on types given in kbase.yaml

This uses the Cerberus library for type validation: http://docs.python-cerberus.org/en/stable/
"""

import inspect
import os
from cerberus import Validator
from functools import wraps

from kbase_sdk.init_context import init_context
import kbase_sdk.param_validation.exceptions as exceptions
from kbase_sdk.param_validation.generate_validators import generate_validators


def validate_params(fn):
    """
    A function decorator that adds parameter validation.
    The function name must be registered in the config and we must be in an SDK repo.
    :param fn: the function we are validating & decorating
    :returns: the wrapper function

    Example usage:
        @validate_params
        def my_method(params):
           ...
    """
    args = inspect.getargspec(fn).args
    if len(args) is not 1:
        raise exceptions.InvalidParamLength()

    @wraps(fn)
    def wrapper(*args, **kwargs):
        context = init_context()
        param_validators = generate_validators(context['config'])
        params = args[0]
        fn_name = fn.__name__
        schema = param_validators.get(fn_name)
        if not schema:
            raise exceptions.MissingMethod(fn_name)
        validator = Validator(schema)
        validator.validate(params)
        if validator.errors:
            raise exceptions.InvalidParams(validator.errors, params)
        return fn(*args, **kwargs)
    return wrapper
