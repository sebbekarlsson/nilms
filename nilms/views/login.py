from flask import Blueprint, render_template, request
from nilms.facades.user_facade import UserFacade
from nilms.password import check_password


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/admin'
)


@bp.route('/login', methods=['POST', 'GET'])
def login():
    err_wrong_cred = 'Wrong credentials'
    errors = []

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        existing = UserFacade.get(name=username)

        if not existing:
            errors.append(err_wrong_cred)

        if not len(errors):
            if not check_password(existing['password'], password):
                errors.append(err_wrong_cred)

    return render_template('admin/login.html', errors=errors)
