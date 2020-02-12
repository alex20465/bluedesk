#!/usr/bin/env python3

from os import path
from distutils.core import setup

current_dir = path.abspath(path.dirname(__file__))
description_file = path.join(current_dir, 'README.md')

if path.exists(description_file):
  with open(path.join(current_dir, 'README.md'), encoding='utf-8') as f:
      long_description = f.read()
else:
  long_description = ""

setup(name='Bluedesk',
      version='1.9',
      scripts=[ 'bin/bluedesk' ],
      description='CLI tool to control lower energy actuator systems (office desks) through bluetooth.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Alexandros Fotiadis',
      author_email='fotiadis90@gmail.com',
      packages=[
        'bluedesk',
        'bluedesk.desks',
        'bluedesk.commands'
      ],
      
      install_requires=[
        "blessings==1.7",
        "bluepy==1.3.0",
        "inquirer==2.6.3",
        "python-editor==1.0.4",
        "readchar==2.0.1",
        "six==1.12.0",
      ]
    )