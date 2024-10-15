from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)
    
    
  # Use 'email' instead of 'emails'
  
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String, nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  
