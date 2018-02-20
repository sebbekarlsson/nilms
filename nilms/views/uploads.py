from flask import Blueprint, send_from_directory
from nilms.config import config


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/uploads'
)


@bp.route('/<path:filename>')
def show(filename):
    return send_from_directory(config['uploads_dir'], filename)
