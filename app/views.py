# app/views.py
from flask import Blueprint
from .controllers import query_tweets

bp = Blueprint('main', __name__)

@bp.route('/q2', methods=['GET'])
def query():
    return query_tweets()

def init_app(app):
    app.register_blueprint(bp)
