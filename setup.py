#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='achtungachtung',
      version='0.0.1',
      description='Reads warnings from warnung.bund.de and transforms them to python objects or json',
      author_email='',
      classifiers=['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                   'Programming Language :: Python :: 3'],
      keywords='alert service',
      packages=find_packages(exclude=['tests']),
      install_requires=['requests'],
      python_requires='>=3',
      entry_points={
        'console_scripts': [
        'achtungachtung=achtungachtung.alertcollector:main',
            ],
        },
       )
