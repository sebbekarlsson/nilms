from nilms.mongo import db
from nilms.views.index import bp as index_bp
from flask import Flask


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)

app.register_blueprint(index_bp)

db = db
