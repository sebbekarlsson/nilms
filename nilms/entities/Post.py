from mongoengine import (
    Document,
    StringField,
    DictField,
    BooleanField,
    DateTimeField
)
import datetime


class Post(Document):
    name = StringField(max_length=200)
    content = StringField()
    is_published = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.now())
    data = DictField()
