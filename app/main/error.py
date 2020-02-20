from flask import url_for, redirect
from . import main


@main.app_errorhandler(401)
def error(error):
    return redirect(url_for('auth.login'), 401)
