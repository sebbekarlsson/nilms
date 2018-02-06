from pymongo import MongoClient
from mongoengine import connect


config = {
    'mongo': {
        'host': 'localhost',
        'db': 'nilms'
    }
}


client = MongoClient(config['mongo']['host'])
DEFAULT_CONNECTION = connect(config['mongo']['db'])


db = client[config['mongo']['db']]
