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
    mimes = {
        '.css': 'text/css',
        '.js': 'text/javascript',
        '.gif': 'image/gif',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.bmp': 'image/bmp',
        '.xml': 'application/xml',
        '.pdf': 'application/pdf'
    }

    filename, ext = os.path.splitext(file_path)
    ext = ext.lower()

    mime = mimes[ext] if ext in mimes else 'text/plain'

    print(mime, ext)

    return send_from_directory(
        os.path.join(config['theme_dir'], 'static'),
        file_path,
        mimetype=mime
    )
