"""
Allows package to be installed in "editable" mode by running `pip install -e`
Can change source code and rerun tests at will
"""
from setuptools import setup, find_packages
from pydo import __version__


setup(name="pydo", packages=find_packages(), version=__version__)
