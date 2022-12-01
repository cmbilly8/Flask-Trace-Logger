from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class LogFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(30000))
    methodName = db.Column(db.String(70))
    date = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    userName = db.Column(db.String(15))
    logFiles = db.relationship('LogFile')