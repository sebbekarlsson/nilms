from flask import session, redirect
from functools import wraps
from bson.objectid import ObjectId
from nilms.facades.user_facade import UserFacade


def is_loggedin():
    return session['user_id'] is not None if 'user_id' in session else False


def get_current_user():
    return UserFacade.get(id=ObjectId(session['user_id'])) if is_loggedin()\
        else None


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not get_current_user():
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function
