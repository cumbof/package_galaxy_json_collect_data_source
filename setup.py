import os
from setuptools import setup, find_packages
import json_collect_data_source # to get the package version number

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='json_collect_data_source',
    version=json_collect_data_source.__version__,
    description='Galaxy JSON Collect Data Source',
    long_description=read('README.md'),
    keywords = "galaxy json collection data source",

    author='Fabio Cumbo',
    author_email='fabio.cumbo@iasi.cnr.it',
    url='https://github.com/fabio-cumbo/package_galaxy_json_collect_data_source',

    install_requires = [],
    packages=find_packages(),
    license = "MIT",
    classifiers=[
        "Development Status :: Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)