#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from setuptools import Extension

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

module1 = Extension('test_spam.spam', sources = ['lib/spam.c'])

setup(
    author="Jie ZHU",
    author_email='zj0512@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Test C extension.",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='test_spam',
    name='test_spam',
    packages=find_packages(include=['test_spam', 'test_spam.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/genzj/test_spam',
    version='0.1.0',
    zip_safe=False,
    ext_modules = [module1],
)
