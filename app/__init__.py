from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from .config import config_options
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
login_manager=LoginManager
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

mail=Mail()
csrf = CSRFProtect()
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager=LoginManager()



def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY'] = "EEE"
    app.config['WTF_CSRF_SECRET_KEY'] = "EEE"
    mail.init_app(app)
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

