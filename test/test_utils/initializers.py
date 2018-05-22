import os
import shutil
import tempfile


def init_temp_app():
    """ Initialize a temporary app and return its context data """
    temp_dir = tempfile.mkdtemp()
    test_app_dir = os.path.join(os.path.dirname(__file__), '..', 'test_app')
    temp_app_dir = os.path.join(temp_dir, 'app')
    shutil.copytree(test_app_dir, temp_app_dir)
    return temp_app_dir
