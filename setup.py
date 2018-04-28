'''
Created on Jul 1, 2017

@author: frmdstryr
@copyright: frmdstryr@gmail.com
@license: MIT

'''
import sys
from setuptools import setup

setup(
    name="pywinutils",
    version="0.1",
    author="frmdstryr",
    author_email="frmdstryr@gmail.com",
    license='MIT',
    url='http://github.com/frmdstryr/pywinutils',
    description="Copy move and delete files using the built in Window's progress dialog",
    long_description=open("README.md").read(),
    py_modules=['winutils'],
    requires=['pywin32'],
    install_requires=['pywin32 >= 218'],
)
