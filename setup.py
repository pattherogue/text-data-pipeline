from setuptools import setup, find_packages

setup(
    name='text-data-pipeline',
    version='1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A text data pipeline for processing, training models, and evaluating results',
    packages=find_packages(),
    install_requires=[
        'pandas',  # Add any dependencies required by your project
        'nltk',
        # Add any other dependencies here
    ],
)
