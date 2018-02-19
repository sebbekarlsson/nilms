from mongoengine import (
    Document,
    StringField,
    DictField,
    BooleanField,
    DateTimeField
)
import datetime


class Page(Document):
    name = StringField(max_length=200)
    template = StringField(max_length=200)
    is_startpage = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now())
    data = DictField()
