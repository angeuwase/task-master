from project import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from project import login_manager

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    hashed_password = db.Column(db.String)
    todolist = db.relationship('Task', backref='master', lazy=True)

    def __init__(self, email, password):
        self.email = email
        self.hashed_password = generate_password_hash(password)

    def is_password_valid(self, password):
        return check_password_hash(self.hashed_password, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def __repr__(self):
        return '<User {}>'.format(self.email)


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

   # def __init__(self, content, date_created=utcdatetinenow, completed=False):
       # self.content = content
       # self.date_created = date_created
       # self.completed = completed
    
    def __repr__(self):
        return '<Task {}'.format(self.id)

    

