from  flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,EqualTo,Email
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email=StringField('Your email address',validators=[DataRequired(),Email()])
    username=StringField('your username',validators=[DataRequired()])
    password=PasswordField('Your password',validators=[DataRequired(),EqualTo('password_confirm',message='password must match')])
    password_confirm=PasswordField('Confirm Passwords',validators=[DataRequired()])
    submit=SubmitField('submit')


    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError("email already exists")

    def validate_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("username already exists")

class LoginForm(FlaskForm):
    email=StringField('Your email address',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('remember me')
    submit=SubmitField('submit')

class BlogForm(FlaskForm):
    title=StringField('Your Title',validators=[DataRequired()])
    content=StringField('Content',validators=[DataRequired()])
    submit = SubmitField('submit')
class CommentForm(FlaskForm):
    comment=StringField('comment',validators=[DataRequired()])
    submit = SubmitField('submit')
class SubscriberForm(FlaskForm):
    email = StringField('Your email address', validators=[DataRequired(), Email()])
    submit = SubmitField('submit')






