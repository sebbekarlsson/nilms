from nilms.entities.Asset import Asset
from nilms.facades.post_facade import PostFacade
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
    def delete(**kwargs):
        try:
            assets = Asset.objects(**kwargs)

            for _asset in assets:
                posts = PostFacade.get_all(
                    query={'assets': _asset}
                )

                for post in posts:
                    if _asset in post.assets:
                        post.assets.remove(_asset)

                    post.update(assets=post.assets)

            return assets.delete()
        except DoesNotExist:
            return False

    @staticmethod
    def get_all(order_by='-created_at', offset=None, limit=None, query={}):
        _all = Asset.objects(**query).skip(offset)\
            .limit(limit).order_by(order_by)

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
