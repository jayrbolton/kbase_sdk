# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)
readme = open(os.path.join(base_dir, 'README.md')).read()

setup(
    name='kbase_sdk',
    description='KBase SDK utilities',
    long_description=readme,
    long_description_content_type="test/markdown",
    python_requires='>=3.5',
    version='0.0.2a3',
    packages=find_packages(),
    install_requires=[
        'pyyaml>=3.12',
        'flask>=1.0.2',
        'cerberus>=1.2',
        'python-dotenv>=0.8.2',
        'coloredlogs>=9.3.1'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers'
    ]
)
