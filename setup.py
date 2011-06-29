from os import path
from setuptools import setup, find_packages

from honey import VERSION

with open(path.join(path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()

setup(
    name='honey',
    version='.'.join(map(str, VERSION)),
    license='Apache License, Version 2.0',
    description='Full drop-in replacement and enhancment for django templates using mako templates.',
    long_description=readme,
    url='https://github.com/bigjason/honey',
    author='Jason Webb',
    author_email='bigjasonwebb@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    keywords='django templates mako',
    classifiers=[
       'Development Status :: 4 - Beta',
       'Topic :: Text Processing :: Markup',
       'Framework :: Django',
       'Operating System :: OS Independent',
       'Intended Audience :: Developers',
       'Programming Language :: Python :: 2.6',
       'Programming Language :: Python :: 2.7',
       'License :: OSI Approved :: Apache Software License'
    ],
    install_requires = [
        'django>=1.2',
        'mako'                        
    ]
)
