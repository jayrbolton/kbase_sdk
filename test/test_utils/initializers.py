from uuid import uuid4
import os
import shutil

import kbase_sdk


def init_temp_app(parent_dir):
    """ Initialize a temporary app and return its context data """
    test_app_dir = os.path.join(os.path.dirname(__file__), '..', 'test_app')
    temp_app_dir = os.path.join(parent_dir, str(uuid4()))
    shutil.copytree(test_app_dir, temp_app_dir)
    return kbase_sdk.init_context(temp_app_dir)
