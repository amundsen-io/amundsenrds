# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from setuptools import find_packages, setup

__version__ = '0.0.1'


requirements = [
    'sqlalchemy>=1.3.0,<2.0'
]

setup(
    name='amundsen-rds',
    version=__version__,
    description='Amundsen ORM Support',
    url='https://www.github.com/amundsen-io/amundsenrds',
    maintainer='Amundsen TSC',
    maintainer_email='amundsen-tsc@lists.lfai.foundation',
    packages=find_packages(),
    dependency_links=[],
    install_requires=requirements,
    python_requires='>=3.6',
    extras_require={},
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
