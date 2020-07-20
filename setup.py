import os

from setuptools import setup

setup(
    name='gameoflife',
    version='1.0.0',
    description='Conway\'s Game of Life implemented with PyGame.',
    packages=['gameoflife'],
    scripts=[
        'bin/gameoflife',
        'bin/gameoflife.bat',
    ],
    zip_safe=False,
    install_requires=[
        'pygame'
    ]
)
