from flask import Blueprint, render_template, redirect, request
from bson.objectid import ObjectId
from nilms.session_utils import login_required
from nilms.theme_utils import get_theme_templates
from nilms.facades.page_facade import PageFacade


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/admin'
)


@bp.route('/')
@login_required
def show():
    return redirect('/admin/dashboard')


@bp.route('/dashboard')
@login_required
def show_dashboard():
    return render_template('admin/dashboard.html')


@bp.route('/pages')
@login_required
def show_pages():
    pages = PageFacade.get_all()

    return render_template('admin/pages.html', pages=pages)


@bp.route('/page/<page_id>', methods=['POST', 'GET'])
@bp.route('/page', defaults={'page_id': None}, methods=['POST', 'GET'])
@login_required
def show_page(page_id):
    page = PageFacade.get(id=ObjectId(page_id)) if page_id else None
    templates = get_theme_templates()

    if request.method == 'POST':
        if request.form.get('submit'):
            name = request.form.get('page-name')
            template = request.form.get('page-template')
            is_startpage = request.form.get('page-is_startpage') is not None

            if not page:
                page = PageFacade.create(
                    name=name,
                    template=template,
                    is_startpage=is_startpage
                )
                return redirect('/admin/page/{}'.format(str(page.id)))
            else:
                page.update(
                    name=name,
                    template=template,
                    is_startpage=is_startpage
                )
                page = PageFacade.get(id=ObjectId(page_id))

    return render_template('admin/page.html', templates=templates, page=page)


@bp.route('/theme-db', methods=['POST', 'GET'])
@login_required
def show_theme_db():
    return render_template('admin/theme_db.html')


@bp.route('/settings')
@login_required
def show_settings():
    return render_template('admin/settings.html')
