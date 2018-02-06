from flask import Blueprint, render_template, redirect


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/admin'
)


@bp.route('/')
def show():
    return redirect('/admin/dashboard')


@bp.route('/dashboard')
def show_dashboard():
    return render_template('admin/dashboard.html')


@bp.route('/pages')
def show_pages():
    return render_template('admin/pages.html')
