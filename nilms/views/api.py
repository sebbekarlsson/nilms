from flask import Blueprint, request, jsonify
from nilms.facades.page_facade import PageFacade
from nilms.facades.post_facade import PostFacade
from nilms.facades.asset_facade import AssetFacade
from nilms.session_utils import login_required
from bson.objectid import ObjectId
from bson.json_util import dumps
import json


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/api'
)


@bp.route('/page/update/<page_id>', methods=['POST', 'GET'])
@login_required
def update_page(page_id):
    if request.method == 'POST':
        query_object = request.get_json()

        kwargs = {
            'data': query_object
        }

        page = PageFacade.get(id=ObjectId(page_id))
        page.update(**kwargs)
        page = PageFacade.get(id=ObjectId(page_id))

        return jsonify(page.data)


@bp.route('/page/data/<page_id>')
def show_page(page_id):
    page = PageFacade.get(id=ObjectId(page_id))

    return jsonify(page.data)


@bp.route('/asset/delete/<asset_id>')
def show_asset_delete(asset_id):
    posts = PostFacade.get_all(
        query={'assets': AssetFacade.get(id=ObjectId(asset_id))}
    )

    for post in posts:
        for asset in post.assets:
            if asset.id == ObjectId(asset_id):
                post.assets.remove(asset)

        post.update(assets=post.assets)

    return jsonify(AssetFacade.delete(id=ObjectId(asset_id)))
