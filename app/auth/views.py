from . import auth
from flask import render_template,redirect,url_for,request,flash
from flask_login import login_required,login_user,logout_user
from .forms import RegistrationForm,LoginForm,commmentForm,PitchForm,TravelForm
from ..models import db,comments,pitch
from ..models import User,pitch
from ..email import email_sender


@auth.route('/auth')

def authorize():
    return render_template('auth/login.html')

@auth.route('/register',methods = ["GET","POST"])


def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(email= form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        email_sender("welcome to pitch","email/welcome",user.email,user=user)

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html',registration_form=form)

@auth.route('/login',methods=["GET","POST"])
def login():
    loginform=LoginForm()
    if loginform.validate_on_submit():
        user=User.query.filter_by(email=loginform.email.data).first()
        if user is not None and user.verify_password(loginform.password.data):
            login_user(user,loginform.remember.data)
            return  redirect(request.args.get('next') or url_for('main.index'))

        flash('invalid username or password')

    return  render_template('auth/login.html',loginform=loginform)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/petrol',methods=['GET','POST'])
@login_required
def get_petroleum():
    return render_template('petroleum.html')

@auth.route('/come',methods=['GET','POST'])
@login_required
def get_comments():
    commentnini=commmentForm()
    if commentnini.validate_on_submit():
        comm=commentnini.comment.data
        popo=comments(comment=comm)
        popo.save_comment()

        return redirect(url_for('main.index'))


    dic = comments.get_yote(id)
    return  render_template('auth/new_comment.html',acha=commentnini,comment=dic)

@auth.route('/pitches',methods = ["GET","POST"])
@login_required
def get_pitches():
    pitchform=PitchForm()
    if pitchform.validate_on_submit():
        pitches=pitchform.pitch.data
        new_pitches=pitch(pitches=pitches)
        new_pitches.save_pitch()

        return  redirect(url_for('main.index'))
    neew=pitch.get_pitch(id)

    return  render_template('pitches.html',pitchform=pitchform,pitch=neew)

@auth.route('/travel',methods = ["GET","POST"])
@login_required
def get_travel():
    travelform=TravelForm()
    if travelform.validate_on_submit():
        travels=travelform.pitch.data
        new_travels=pitch(pitches=travels)
        new_travels.save_pitch()

        return  redirect(url_for('main.index'))
    neew=pitch.get_pitch(id)

    return render_template('travel.html',pitch=neew,travelform=travelform)






