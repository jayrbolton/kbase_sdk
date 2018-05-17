
class ConfigInvalidException(Exception):
    """ Some part of the kbase.yaml file is invalid acccording to the schemas found in ./validate_yaml.py """

    def __init__(self, given_config, general_error, key_errors):
        self.given_config = given_config
        self.general_error = general_error
        self.key_errors = key_errors


class MissingPathException(Exception):
    """ A path, such as src/main.py or test/test_main.py, is missing from the project """

    def __init__(self, path, name):
        self.path = path
        self.name = name
