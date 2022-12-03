from flask import Blueprint
from flaskinit import db

us = Blueprint('us', __name__)


@us.route('/index')
def index():
    db.session.add()
    return 'index'