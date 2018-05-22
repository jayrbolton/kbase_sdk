"""
Validate that the methods registered in kbase.yaml match those found in src/main.py
Also validate that the parameters for every method match a certain form

TODO Can also validate whether each method has a docstring
"""

import importlib.util as import_util
import inspect


def validate_main_methods(context):
    """
    Validate that the methods found in kbase.yaml are present in main.py
    Does some introspection on functions in main.py to validate their names and parameters
    Will log errors and exit if any validations fail
    :param context: the context data from the init_context module
    """
    module_path = context['paths']['main_module']
    spec = import_util.spec_from_file_location('main', module_path)
    main = import_util.module_from_spec(spec)
    spec.loader.exec_module(main)
    functions = inspect.getmembers(main, predicate=inspect.isfunction)
    # Provide fallback dictionaries for the methods
    # We can't use config.get('narrative_methods', {}) as that key can be actually set to None
    narrative_methods = context['config'].get('narrative_methods') or {}
    direct_methods = context['config'].get('direct_methods') or {}
    methods = {**narrative_methods, **direct_methods}
    # Keep track of all method names we find in main.py
    found_methods = {}
    for name, func in functions:
        if name in methods:
            found_methods[name] = True
    # Find all methods in config that are missing in Main
    for name in methods:
        if not found_methods.get(name):
            raise MissingAppFunction(name)


def _param_error_msg(expected, args):
    """ Log an error where there is a mismatch between expected and actual parameters """
    return '  Parameters should be ' + expected + '. Current params are ' + '(' + ', '.join(args) + ')'


class MissingAppFunction(Exception):
    """ A function registered in kbase.yaml is not found in main.py """

    def __init__(self, fn_name):
        self.fn_name = fn_name
