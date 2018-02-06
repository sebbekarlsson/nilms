from podmosphere.entities.page import Page
from mongoengine.queryset import DoesNotExist
from nilms.mongo import db


class PageFacade(object):
    @staticmethod
    def get_by_ids(ids):
        return db.page.find({
            '_id': {'$in': ids}
        })

    @staticmethod
    def get(name):
        return Page.objects.get(name=name)

    @staticmethod
    def get_all():
        return Page.objects().order_by('name')

    @staticmethod
    def create(name):
        c = Page(name=name)
        c.save()

        return c

    @staticmethod
    def exists(name):
        try:
            return Page.objects.get(name=name) is not None
        except DoesNotExist:
            return False
