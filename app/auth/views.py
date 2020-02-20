from . import auth
from flask import render_template,redirect,url_for,request,flash
from flask_login import login_required,login_user,logout_user
from .forms import RegistrationForm,LoginForm,CommentForm,BlogForm
from ..models import db,Comments,Blog,User
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



@auth.route('/blog/<int:blog_id>',methods=['GET','POST'])
@login_required
def get_comments(blog_id):
    commentnini=CommentForm()
    blog = Blog.query.filter_by(id=blog_id).first()
    if commentnini.validate_on_submit():

        popo=Comments(comment=commentnini.comment.data,blogr=blog)
        db.session.add(popo)
        db.session.commit()
    rada = Comments.query.filter_by(blogr=blog).all()

    return  render_template('auth/new_comment.html',acha=commentnini,blog=blog,rada=rada)

@auth.route('/blogform',methods = ["GET","POST"])
@login_required
def get_blogs():
    blogform=BlogForm()
    if blogform.validate_on_submit():
        title=blogform.title.data
        content=blogform.content.data
        new_blog=Blog(title=title,content=content)
        new_blog.save_blog()

        return  redirect(url_for('main.index'))


    return  render_template('pitches.html',blogform=blogform)








