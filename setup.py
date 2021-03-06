from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='basicsudoku',
    version=__import__('basicsudoku').__version__,
    url='https://github.com/asweigart/basicsudoku',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description=('A simple, basic Sudoku class in Python. Suitable for programming tutorials or experimentation.'),
    license='BSD',
    long_description=long_description,
    packages=['basicsudoku'],
    test_suite='tests',
    install_requires=[],
    keywords="sudoku",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)