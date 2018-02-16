from flask import Blueprint, send_from_directory
from nilms.config import config
import os


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/theme'
)


@bp.route('/static/<path:file_path>')
def show_file(file_path):
    return send_from_directory(
        os.path.join(config['theme_dir'], 'static'),
        file_path
    )
