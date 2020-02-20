from flask import url_for, redirect,render_template
from . import main
from flask import flash


@main.app_errorhandler(401)
def error(error):

    return redirect(url_for('auth.login'))