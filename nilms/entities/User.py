from mongoengine import Document, StringField, ReferenceField
from nilms.entities.Asset import Asset


class User(Document):
    name = StringField(max_length=120, unique=True)
    password = StringField(min_length=5)
    avatar = ReferenceField(Asset)
