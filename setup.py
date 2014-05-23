#coding: utf-8
import os
from setuptools import setup

setup(
    name = "wolframalpha-cli",
    version = "0.1",
    author = "Fernando Xavier de Freitas Crespo",
    author_email = "fernando82@gmail.com",
    description = ("Command Line Interface to run queries on WolframAlpha"),
    long_description = "".join(open('README.md').readlines()),
    license = "MIT",
    keywords = "wolframalha cli python utility",
    url = "https://github.com/fcrespo82/wolframalpha-cli",
    py_modules = ['wolframalpha'],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires = open('requirements.txt').readlines(),
    entry_points = {
        'console_scripts': ['wolframalpha-cli = wolframalpha:main',
                            'wa-cli = wolframalpha:main']
    },
)
