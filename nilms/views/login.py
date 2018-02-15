from flask import Blueprint, render_template, request
from nilms.facades.user_facade import UserFacade


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/admin'
)


@bp.route('/login', methods=['POST', 'GET'])
def login():
    errors = []

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        existing = UserFacade.get(name=username)

        if not existing:
            errors.append('Wrong credentials')

    return render_template('admin/login.html', errors=errors)
