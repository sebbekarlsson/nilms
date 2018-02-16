from mongoengine import Document, StringField, DictField, BooleanField


class Post(Document):
    name = StringField(max_length=200)
    content = StringField()
    is_published = BooleanField(default=True)
    meta = DictField()
