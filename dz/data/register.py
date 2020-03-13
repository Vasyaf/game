import datetime
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,TextAreaField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
import sqlalchemy #, flask_login
#from .db_session import SqlAlchemyBase
from sqlalchemy import orm
#from werkzeug.security import generate_password_hash, check_password_hash




class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Войти')
    news = orm.relation("News", back_populates='user')
    
    #def set_password(self, password):
        #self.hashed_password = generate_password_hash(password)
    
    #def check_password(self, password):
        #return check_password_hash(self.hashed_password, password)     
   