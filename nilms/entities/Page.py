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


class Page(Document):
    name = StringField(max_length=200)
    template = StringField(max_length=200)
    is_startpage = BooleanField(default=False)
    assets = ListField(ReferenceField('Asset'))
    created_at = DateTimeField(default=datetime.datetime.now())
    data = DictField()

    def get_asset(self, name):
        for asset in self.assets:
            if asset.name == name:
                return asset
