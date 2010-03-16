#!/usr/bin/env python

from setuptools import setup

setup(name='quicktext',
      version='0.1',
      description='GTK quick message popup tool',
      author='Ali Scott',
      author_email='ali.scott@gmail.com',
      scripts = ['scripts/quicktext.py'],
      entry_points = {
          'console_scripts': ['quicktext = quicktext:main']
      })
