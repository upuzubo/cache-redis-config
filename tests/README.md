# Project: cache-redis-config
# Author: [Your Name]
# Date: [Today's Date]

from setuptools import setup

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setup(
    name='cache-redis-config',
    version='1.0.0',
    description='A package for caching with Redis configuration',
    author='[Your Name]',
    author_email='[Your Email]',
    install_requires=install_requires
)