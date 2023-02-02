from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='overlab',
    packages=find_packages(),
    version='0.2.3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Francesco Gualdi',
    license='GPL'
)
