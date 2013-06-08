from distutils.core import setup
from setuptools import find_packages

setup(
    name='oaxmlapi',
    version='1.0',
    author='Ryan Morrissey',
    author_email='contactme@ryancmorrissey.com',
    packages=find_packages(),
    url='https://github.com/23maverick23/oaxmlapi',
    license='LICENCE.md',
    description='A Python wrapper around the NetSuite OpenAir XML API.',
    long_description=open('README.md').read(),
    install_requires=[
        "pytest >= 2.3.5",
    ],
    zip_safe=False,
)
