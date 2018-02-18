from flask import render_template
from nilms.session_utils import is_loggedin


def admin_navigation(page_id):
    if not is_loggedin():
        return render_template('editing/visitor.html', page_id=page_id)

    return render_template('editing/admin_navigation.html', page_id=page_id)
