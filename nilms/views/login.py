from flask import Blueprint, render_template  # , render_template, redirect


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/admin'
)


@bp.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('admin/login.html')
