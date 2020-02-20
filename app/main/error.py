from flask import url_for, redirect,render_template
from . import main
from flask import flash
from app.auth.forms import LoginForm


@main.app_errorhandler(401)
def error(error):
    loginform=LoginForm()
    return render_template('auth/login.html',loginform=loginform)