from mongoengine import Document, StringField, DictField, BooleanField


class Page(Document):
    name = StringField(max_length=200)
    template = StringField(max_length=200)
    is_startpage = BooleanField(default=False)
    data = DictField()
