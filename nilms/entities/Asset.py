from mongoengine import (
    Document,
    StringField,
    DateTimeField
)
import datetime


class Asset(Document):
    name = StringField(max_length=200)
    filename = StringField()
    created_at = DateTimeField(default=datetime.datetime.now())
