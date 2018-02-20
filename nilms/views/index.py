from flask import Blueprint
from nilms.facades.page_facade import PageFacade
from nilms.facades.post_facade import PostFacade
from nilms.facades.asset_facade import AssetFacade
from nilms.config import config
from nilms.theme_utils import get_theme_db
from nilms.editing_utils import admin_navigation
from jinja2 import Environment, FileSystemLoader
import os


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/<page_name>')
@bp.route('/', defaults={'page_name': None})
def show(page_name):
    page = PageFacade.get(name=page_name) if page_name\
        else PageFacade.get(is_startpage=True)

    if not page:
        return 'page not found', 404

    env = Environment(
        loader=FileSystemLoader(os.path.join(config['theme_dir'], 'templates'))
    )

    env.globals.update(
        admin_navigation=admin_navigation,
        PageFacade=PageFacade,
        PostFacade=PostFacade,
        AssetFacade=AssetFacade
    )

    j_template = env.get_template(page.template)

    return j_template.render(db=get_theme_db(), page=page)
