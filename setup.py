from setuptools import setup
import codecs
import os


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


long_description = read('README.md')

setup(
    name='forif',
    version='0.0.1',
    py_modules=['forif'],
    url='https://github.com/tzickel/forif',
    license='WTFPLApache License 2.0',
    author='tzickel',
    author_email='',
#    tests_require=['nose'],
    description='A C-like condition assignment syntax in python',
    long_description=long_description,
    platforms='any',
#    test_suite='nose.collector',
    test_suite='tests.TestForIf',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
#    extras_require={
#        'testing': ['nose'],
#    }
)
