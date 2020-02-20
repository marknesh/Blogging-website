from . import main
from flask import render_template,abort
from flask_login import login_required
from ..models import User,Blog




@main.route('/')
def index():
    neew=Blog.get_blog(id)
    return render_template('home.html',pitch=neew)



@main.route('/user/<jina>',methods=['GET','POST'])
def profile(jina):
    user=User.query.filter_by(username= jina).first()
    if user is None:
        abort(404)
    pitchess = pitch.get_pitch(id)
    return  render_template('profile/profile.html',user=user,lol=pitchess)

