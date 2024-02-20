from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='1.0',
    description='Description of your project',
    author='Your Name',
    author_email='your_email@example.com',
    packages=find_packages(),
    install_requires=[
        'nltk',  # Add NLTK as a dependency
        # Add any other dependencies here
    ],
)
