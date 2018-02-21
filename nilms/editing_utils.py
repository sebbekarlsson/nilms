from flask import render_template
from nilms.session_utils import is_loggedin


def admin_navigation(post, page):
    if not is_loggedin():
        return render_template('editing/visitor.html', post=post, page=page)

    return render_template('editing/admin_navigation.html',
                           post=post, page=page)
