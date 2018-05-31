
class InvalidRunAppParams(Exception):

    def __init__(self, errs):
        self.errors = errs

    def __str__(self):
        return "Invalid parameters to kbase_sdk.run_app: " + str(self.errors)
