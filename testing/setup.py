# -*- coding: utf-8 -*-
"""Setup for CS410-Project."""
from setuptools import setup, find_packages


requires = [
        'scikit-learn',
        'numpy',
        'nltk',
        'matplotlib',
        'pandas',
        'scipy',
        ]

setup(
        name='CS410-Project',
        description='CS410-Fa17-Yelp Context Analysis',
        author='Team47',
        url='https://github.com/ileanmjr88/CS410-Project',
        packages=find_packages(),
        install_requires=requires,
        tests_require=requires,
        )
