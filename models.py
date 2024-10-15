from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()
# Association table
user_groups = db.Table('user_groups',
                      db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                      db.Column('group_id', db.Integer, db.ForeignKey('groups.id'))
                      )

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship('Post', back_populates='user')
    groups = db.relationship("Group", secondary = user_groups,back_populates="users")
    
    @validates('address')
    def  validate_address(self, key, address):
        if '@' not in address:
            raise ValueError("Invalid email address")
        return address
    
    
  # Use 'email' instead of 'emails'
  
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('User', back_populates='posts')  
    
    
class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    users = db.relationship("User", secondary = user_groups, back_populates="groups")