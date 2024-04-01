from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='image_processing',
    version='0.0.1',
    author='Julio Lima',
    description='Image Processing Package using Skimage',
    long_description=page_description,
    long_description_content_type='text/markdow',
    
)