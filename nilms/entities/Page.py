from mongoengine import Document, StringField


class Page(Document):
    name = StringField(max_length=200, required=True, unique=True)
