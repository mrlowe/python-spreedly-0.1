import os
import sys
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def run_tests():
    sys.path.append(os.path.join(os.path.dirname(__file__), 'tests'))
    from test_spreedly import suite
    return suite()


setup(
    name="python-spreedly",
    version="0.1",
    url='http://github.com/willowtreeapps/python-spreedly',
    license='MIT',
    description="A python API for the spreedly subscription service.",
    packages=['spreedly'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='__main__.run_tests'
)
