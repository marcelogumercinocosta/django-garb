import setuptools
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-garb',
    version="2020.4.1",
    author='Marcelo Gumercino Costa',
    author_email='marcelogc@gmail.com',
    description='Modern theme for Django admin interface.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/marcelogumercinocosta',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ],
    python_requires='>=3.6',
)