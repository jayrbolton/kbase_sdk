

class InvalidParams(Exception):
    """ Some parameters passed to an app method are invalid according to the types in kbase.yaml """

    def __init__(self, errors, params):
        self.errors = errors
        self.params = params


class InvalidParamLength(Exception):
    """ Parameters to an app function are invalid """
    pass


class MissingMethod(Exception):
    """ A validated method in main.py is missing from kbase.yaml """

    def __init__(self, method_name):
        self.method_name = method_name
