#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:14:54 2024

@author: 4vt
"""

import setuptools

setuptools.setup(name="deepIso",
                 version="0.0.0",
                 url="https://github.com/stavis1/deepIso",
                 package_dir={"": "src"},
                 packages=setuptools.find_namespace_packages(where="src"),
                 include_package_data=True,
                 license_files=['LICENSE'],
                 classifiers=['Programming Language :: Python :: 3.12'],
                 python_requires='==3.12.4')

