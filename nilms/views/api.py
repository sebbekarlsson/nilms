from flask import Blueprint


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/api'
)


@bp.route('/page/<page_id>/<action>', methods=['POST', 'GET'])
@bp.route('/page', defaults={'page_id': None, 'action': None})
def show_page(page_id, action):
    return 'not implemented'
