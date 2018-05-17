"""
General exception classes
"""


class DependencyException(Exception):
    """ Missing dependency, such as docker or git """

    def __init__(self, dep_name):
        self.dep_name = dep_name


class NotAppException(Exception):
    """ Not in an app project directory """
    pass
