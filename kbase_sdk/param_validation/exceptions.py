

class ParamValidationException(Exception):

    def __init__(self, errors, params):
        self.errors = errors
        self.params = params


class InvalidParamLength(Exception):
    """ Parameters to an app function are invalid """
    pass
