from nilms.entities.Post import Post
from mongoengine.queryset import DoesNotExist
from nilms.mongo import db


class PostFacade(object):
    @staticmethod
    def get_by_ids(ids):
        return db.post.find({
            '_id': {'$in': ids}
        })

    @staticmethod
    def get(**kwargs):
        try:
            return Post.objects.get(**kwargs)
        except DoesNotExist:
            return None

    @staticmethod
    def get_all(order_by='-created_at', offset=None, limit=None, query={}):
        _all = Post.objects(**query).skip(offset).limit(limit).order_by(order_by)

        return _all

    @staticmethod
    def create(**kwargs):
        c = Post(**kwargs)
        c.save()

        return c

    @staticmethod
    def exists(**kwargs):
        try:
            return Post.objects.get(**kwargs) is not None
        except DoesNotExist:
            return False
