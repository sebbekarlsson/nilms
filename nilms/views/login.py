from flask import Blueprint, render_template, request


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/admin'
)


@bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        return str((username, password))

    return render_template('admin/login.html')
