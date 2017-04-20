from setuptools import setup

setup(
    name='algolia-analytics',
    description='Python interface for the Algolia Analytics REST API',
    version='0.1',
    packages=['algolia_analytics'],
    test_suite='tests',
    tests_require=[
        'mock',
    ],
    install_requires=[
        'requests',
    ],
)

