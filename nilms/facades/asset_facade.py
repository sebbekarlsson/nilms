from nilms.entities.Asset import Asset
from mongoengine.queryset import DoesNotExist


class AssetFacade(object):
    @staticmethod
    def get_by_ids(ids):
        return Asset.objects(id__in=ids)

    @staticmethod
    def get(**kwargs):
        try:
            return Asset.objects.get(**kwargs)
        except DoesNotExist:
            return None

    @staticmethod
    def get_all(order_by='-created_at', offset=None, limit=None):
        _all = Asset.objects().skip(offset).limit(limit).order_by(order_by)

        return _all

    @staticmethod
    def create(**kwargs):
        c = Asset(**kwargs)
        c.save()

        return c

    @staticmethod
    def exists(**kwargs):
        try:
            return Asset.objects.get(**kwargs) is not None
        except DoesNotExist:
            return False
