from setuptools import setup


setup(
    name='nilms',
    version='0.1',
    install_requires=[
        'flask',
        'flask_assets',
        'pymongo',
        'mongoengine',
        'jsmin'
    ],
    packages=[
        'nilms'
    ],
    entry_points={
        'console_scripts': [
        ]
    }
)
