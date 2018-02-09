from mongoengine import Document, StringField


class User(Document):
    name = StringField(max_length=120, unique=True)
    password = StringField(min_length=5)
