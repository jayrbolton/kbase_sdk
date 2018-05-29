kbase_sdk
=========

Core utilities for KBase SDK apps. **Note: experimental**


Installation
------------

.. code:: sh

    $ pip install --extra-index-url https://test.pypi.org/simple kbase_sdk

This package currently only lives in test PyPi

Usage
-----

*Initialize app context*

.. code:: python

    import kbase_sdk

    context = kbase_sdk.init_context()

    # You can also explicitly pass in the root directory of your app
    # Useful if it is not your current working directory
    context = kbase_sdk.init_context(root_directory)


*Run another app as a remote job*

.. code:: python

    import kbase_sdk

    job = kbase_sdk.run_app(context, {
        app: 'AssemblyUtil',
        method: 'get_assembly_as_fasta',
        params: { 'ref': 'x/y/z' }
    })


Development
-----------

Before working, activate a virtualenv with python3 and install
dependencies

.. code:: sh

    # Init the virtual environment
    $ python3 -m venv env
    $ source env/bin/activate

    # Install package dependencies
    $ pip install -e .

    # Install dev dependencies
    $ pip install -r dev-requirements.txt

Tests
~~~~~

.. code:: sh

    # Make sure you are in a virtualenv
    $ source env/bin/activate
    # Make sure dependencies are installed
    $ pip install -e .
    $ pip install -r dev-requirements.txt

    # Run all tests
    $ make test

    # Run a single test module
    $ python -m unittest test/test_something.py

Build
^^^^^

Pip

.. code:: sh

    # Generates a build file into dist/
    $ python setup.py bdist_wheel 
    # Uploads the build to pypi
    $ twine upload --repository-url https://test.pypi.org/legacy/ dist/x

Project anatomy
---------------

The python packages are found in ``/kbase_sdk/``. Tests are found in ``/test/``.

Key files:

-  ``Makefile`` -- targets for testing and publishing
-  ``setup.py`` -- python setuptools configuration for pip packaging
-  ``conda_recipe`` -- config for conda packaging
