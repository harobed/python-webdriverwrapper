#!/usr/bin/env python
import os, re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

v = open(os.path.join(here, 'webdriverwrapper', '__init__.py'))
VERSION = re.compile(r".*VERSION = '(.*?)'", re.S).match(v.read()).group(1)
v.close()


setup(
    name='webdriverwrapper',
    version=VERSION,
    packages=['webdriverwrapper'],

    install_requires=[line.strip() for line in open('requirements.txt').readlines() if line],

    url='https://github.com/horejsek/python-webdriverwrapper',
    author='Michal Horejsek',
    author_email='horejsekmichal@gmail.com',
    description='Better interface for WebDriver (Selenium 2).',
    license='PSF',

    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
)
