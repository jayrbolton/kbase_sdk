"""
Validate the existence of all the boilerplate directories and files in an app
"""

from .exceptions import MissingPathException
import os


def validate_paths(paths):
    """ Validate the existence of every standard project directory and file """
    for (name, path) in paths.items():
        if not os.path.exists(path):
            raise MissingPathException(path, name)
