from setuptools import setup


setup(
    name='nilms',
    version='0.1',
    install_requires=[
        'wtforms',
        'flask_assets',
        'pymongo',
        'mongoengine',
        'jsmin',
        'flask',
        'bcrypt'
    ],
    packages=[
        'nilms'
    ],
    entry_points={
        'console_scripts': [
            'nilms-init = nilms.initialize:init'
        ]
    }
)
