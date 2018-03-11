from nilms.mongo import db
from nilms.views.index import bp as index_bp
from nilms.views.admin import bp as admin_bp
from nilms.views.login import bp as login_bp
from nilms.views.api import bp as api_bp
from nilms.views.theme import bp as theme_bp
from nilms.views.uploads import bp as uploads_bp
from nilms.theme_utils import get_theme_db
from nilms.session_utils import get_current_user
from flask import Flask


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)

app.register_blueprint(index_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(login_bp)
app.register_blueprint(api_bp)
app.register_blueprint(theme_bp)
app.register_blueprint(uploads_bp)

app.jinja_env.globals.update(
    get_theme_db=get_theme_db,
    get_current_user=get_current_user,
    isinstance=isinstance,
    basestring=basestring
)

db = db
