from nilms.config import config
from pymongo import MongoClient
from mongoengine import connect


client = MongoClient(config['mongo']['host'])
DEFAULT_CONNECTION = connect(config['mongo']['db'])


db = client[config['mongo']['db']]
