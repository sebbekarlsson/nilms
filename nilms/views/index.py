from flask import Blueprint
from nilms.facades.page_facade import PageFacade
from nilms.facades.post_facade import PostFacade
from nilms.facades.asset_facade import AssetFacade
from nilms.config import config
from nilms.theme_utils import get_theme_db
from nilms.editing_utils import admin_navigation
from jinja2 import Environment, FileSystemLoader
import os
from bson.objectid import ObjectId


bp = Blueprint(__name__, __name__, template_folder='templates')


env = Environment(
    loader=FileSystemLoader(os.path.join(config['theme_dir'], 'templates'))
)

env.globals.update(
    admin_navigation=admin_navigation,
    PageFacade=PageFacade,
    PostFacade=PostFacade,
    AssetFacade=AssetFacade
)


@bp.route('/<page_name>')
@bp.route('/', defaults={'page_name': None})
def show(page_name):
    page = PageFacade.get(name=page_name) if page_name\
        else PageFacade.get(is_startpage=True)

    if not page:
        return 'page not found', 404

    j_template = env.get_template(page.template)

    return j_template.render(db=get_theme_db(), page=page)


@bp.route('/post/<post_id>')
@bp.route('/', defaults={'post_id': None})
def show_post(post_id):
    post = PostFacade.get(id=ObjectId(post_id)) if post_id else None

    if not post:
        return 'post not found', 404

    j_template = env.get_template(post.template)

    return j_template.render(db=get_theme_db(), post=post, page=post)
