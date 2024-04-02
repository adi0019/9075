from setuptools import setup, find_packages

setup(
    name='app',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        # Add any additional dependencies required by your Flask app here
        'textblob'

    ],
)
