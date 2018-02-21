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
    fields = DictField()

    def get_asset(self, name):
        for asset in self.assets:
            if asset.name == name:
                return asset

    def get_field(self, name):
        for k, v in self.fields.items():
            realname = k.split('template-field_')[1]

            if name == realname:
                return v
