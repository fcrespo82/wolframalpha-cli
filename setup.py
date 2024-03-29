#coding: utf-8
import os
from setuptools import setup

from distutils.core import setup

setup(
    name = "wolframalpha-cli",
    version = "1.1.0",
    description = ("Command Line Interface to run queries on WolframAlpha"),
    long_description = "".join(open('README.md').readlines()),
    long_description_content_type = "text/markdown",
    author = "Fernando Xavier de Freitas Crespo",
    author_email = "fernando82@gmail.com",
    license = "MIT",
    keywords = "wolframalpha cli python utility",
    url = "https://github.com/fcrespo82/wolframalpha-cli",
    py_modules = ['wolframalpha'],
    classifiers = [
        "Environment :: Console",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires = open('requirements.txt').readlines(),
    entry_points = {
        'console_scripts': ['wolframalpha-cli = wolframalpha:main',
                            'wa-cli = wolframalpha:main',
                            'wa = wolframalpha:main']
    },
)
