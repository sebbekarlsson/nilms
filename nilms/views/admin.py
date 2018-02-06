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


@bp.route('/page')
def show_page():
    return render_template('admin/page.html')


@bp.route('/settings')
def show_settings():
    return render_template('admin/settings.html')
