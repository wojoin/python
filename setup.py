# -*- coding: utf-8 -*-
# Project Name  : Python 
# File Name     : setup.py
# Author        : 细嗅蔷薇
# Date Time     : 2016/9/27 21:21
# Description   :
# Version       : 1.0.1

from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)