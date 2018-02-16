from flask import Blueprint
from nilms.facades.page_facade import PageFacade
from nilms.config import config
from jinja2 import Environment, FileSystemLoader
import os


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/<page_name>')
def show(page_name):
    page = PageFacade.get(name=page_name)

    if not page:
        return 'page not found', 404

    env = Environment(
        loader=FileSystemLoader(os.path.join(config['theme_dir'], 'templates'))
    )

    j_template = env.get_template(page.template)

    return j_template.render()
