from mongoengine import Document, StringField, DictField


class Page(Document):
    name = StringField(max_length=200)
    template = StringField(max_length=200)
    data = DictField()
