from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import models

# db必须在view前面实例化出来
db = SQLAlchemy()
session = Session()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.DevConfig')

    db.init_app(app)
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(userid):
        return models.User.get(userid)

    # flask-session, first step
    # session.init_app(app)

    from .views.account import ac
    app.register_blueprint(ac)
    from .views.user import us
    app.register_blueprint(us)

    return app