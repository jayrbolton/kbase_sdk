"""
Initialize the contextual data for an app, such as file-paths, configuration
data, environment data, etc.
"""

import yaml
import shutil
import functools
import os
import dotenv

from .config_validation.validate_yaml import validate_yaml
from .config_validation.validate_paths import validate_paths
from .config_validation.exceptions import ConfigInvalid
import kbase_sdk.exceptions as exceptions

dotenv.load_dotenv(dotenv_path='./.env')


@functools.lru_cache(maxsize=1)
def init_context(directory=None):
    """
    Initialize an app's context data from anywhere within the app.
    This function is memoized, so we don't have to redo the same IO on every
    call, and we can call it repeatedly from different modules without
    worrying.
    """
    # Test for executable dependencies
    for dep in ['docker']:
        if not shutil.which(dep):
            raise exceptions.DependencyException(dep)
    root_path = directory or os.getenv('KBASE_ROOT') or os.getcwd()
    config_path = os.path.join(root_path, 'kbase.yaml')
    paths = {
        'root': root_path,
        'config': config_path,
        'main_module': os.path.join(root_path, 'src', 'main.py'),
        'src_dir': os.path.join(root_path, 'src'),
        'test_dir': os.path.join(root_path, 'test'),
        'test_main_module': os.path.join(root_path, 'test', 'test_main.py')
    }
    validate_paths(paths)
    config = _load_config(config_path)
    validate_yaml(config)
    context = {
        'paths': paths,
        'config': config,
        'docker_image_name': 'kbase-apps/' + config['module']['name'],
        'username': os.getenv('KBASE_USERNAME'),
        'token': os.getenv('KBASE_TOKEN')
    }
    return context


def _load_config(config_path):
    """ Load the YAML configuration file into a python dictionary """
    with open(config_path, 'r') as stream:
        config = yaml.load(stream)  # Throws yaml.YAMLError
        if not isinstance(config, dict):
            # Handles the case if the yaml is a single string, array, etc
            raise ConfigInvalid(config, 'should be a dict', [])
    return config
