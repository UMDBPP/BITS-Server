import sys
import os
import fnmatch
from setuptools import setup, Extension


setup(
    name="bits",
    version="0.1.0",
    include_package_data=True,
    author='Univeristy of Maryland Space Systems Laboratory Balloon Payload Program',
    author_email='nearspace@ssl.umd.edu',
    packages=['bits'],
    zip_safe=False,
    url='http://nearspace.umd.edu',
    license='MIT',
    description='Server segment for Balloon Iridium Telemetry System',
    install_requires=[
        "Flask",
        "strict-rfc3339",
        "gunicorn",
    ],
)

