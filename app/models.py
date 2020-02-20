from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from .  import login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255), unique=True, index=True)
    username = db.Column(db.String(255))
    secure_password=db.Column(db.String(255))





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
    comments=db.relationship('Comments',backref='blogr',lazy="dynamic")



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

    @classmethod
    def get_yote(cls,id):
        coke=Comments.query.filter_by().all()
        return coke






