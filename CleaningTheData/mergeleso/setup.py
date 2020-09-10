# -*- coding: uft-8 -*-

# This is where you set up your python code to be packaged.
# When ready, check out:
#   https://github.com/navdeep-G/setup.py
#   https://packaging.python.org/

'''
Other files you will need:
  LICENSE (see github repo)
  MANIFEST.in
  Makefile

'''

# https://kenreitz.org/essays/repository-structure-and-python

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.0.1',
    descriptioin='Trying leso data code',
    author='Barb Hawes',
    author_email='somewhere@here',
    url='https://github.com/bh1207/project0',
    license=license,
    packages=find_packages(exclude=('tests','docs')))
