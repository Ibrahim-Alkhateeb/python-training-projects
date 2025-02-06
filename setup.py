from setuptools import setup, find_packages

setup(
    name='taskaty',
    version='0.1.0',
    description='A simple command-line Task-app written in Python',
    author='Ibrahim Khateeb',
    packages=find_packages(),
    install_requires=['tabulate'],
    entry_points={
        'console_scripts': [
            'taskaty=taskaty.app:main',  # Make sure this is correct
        ],
    },
)
