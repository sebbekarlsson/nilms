from mongoengine import (
    Document,
    StringField,
    DictField,
    BooleanField,
    DateTimeField,
    ListField,
    ReferenceField
)
import datetime


class Post(Document):
    name = StringField(max_length=200)
    content = StringField()
    template = StringField(max_length=200)
    is_published = BooleanField(default=True)
    assets = ListField(ReferenceField('Asset'))
    created_at = DateTimeField(default=datetime.datetime.now())
    data = DictField()

    def get_field(self, name):
        '''
        There is currently no plan for fields in Post
        '''
        return None
