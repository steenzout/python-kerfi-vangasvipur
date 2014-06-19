#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kerfi.package


from pip.req import parse_requirements

from setuptools import find_packages, setup

setup(name='kerfi-vangasvipur',
      version=kerfi.package.__version__,
      description='Python tools to manipulate information retrieved from OSX system_profiler.',
      author='Pedro Salgado',
      author_email='steenzout@ymail.com',
      maintainer='Pedro Salgado',
      maintainer_email='steenzout@ymail.com',
      url='https://github.com/steenzout/python-kerfi-vangasvipur',
      packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
      install_requires=[str(pkg.req) for pkg in parse_requirements('requirements.txt')],
      tests_requires=[str(pkg.req) for pkg in parse_requirements('test-requirements.txt')],)
