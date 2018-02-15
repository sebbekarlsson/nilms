import json


config = {}
with open('config.json') as _file:
    config = json.loads(_file.read())
_file.close()
