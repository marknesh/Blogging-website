from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from .  import login_manager
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255), unique=True, index=True)
    username = db.Column(db.String(255))
    secure_password=db.Column(db.String(255))
    blogs=db.relationship('Blog',backref='users',lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('you cannot this attribute password')

    @password.setter


    def password(self,password):
        self.secure_password=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.secure_password,password)

class Blog(db.Model):
    __tablename__='blogs'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255))
    content = db.Column(db.String(255))
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    comments=db.relationship('Comments',backref='blogr',lazy="dynamic")
    user_id=db.Column(db.Integer,db.ForeignKey('person.id'))


    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod


    def get_blog(cls,id):
        eka=Blog.query.filter_by().all()
        return eka

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

class Comments(db.Model):
    __tablename__='comments'
    id =db.Column(db.Integer, primary_key=True)
    comment=db.Column(db.String(255))
    blogr_id=db.Column(db.Integer,db.ForeignKey('blogs.id'))



    def save_comment(self):
        db.session.add(self)
        db.session.commit()

class Subscriber(db.Model):
    __tablename__ = 'subscriber'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255), unique=True, index=True)

class Qoutes:
    def __init__(self,id,author,quote):
        self.id = id
        self.author=author
        self.quote=quote













