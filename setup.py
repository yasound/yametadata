#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

required = ['requests',]

packages = [
    'yametadata',
]

setup(
    name='radioways',
    version='0.1',
    description='radioways api',
    long_description=open('README.markdown').read() + '\n\n' +
                     open('HISTORY.markdown').read(),
    author='Jérôme Blondon',
    author_email='jerome@yasound.com',
    url='https://github.com/yasound/radioways',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    include_package_data=True,
    install_requires=required,
    license='Proprietary',
    classifiers=(
    ),
)


