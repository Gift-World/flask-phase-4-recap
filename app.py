from flask import Flask, make_response,request
from flask_migrate import Migrate
from models import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///recap.db"

# Initialize the database with the app
migrate = Migrate(app, db)
db.init_app(app)

# Initialize Flask-Migrate with the app and db
@app.route('/users', methods=['POST','GET'])
def users():
    if request.method=='GET':    
        response = [user.to_dict() for user in User.query.all()]
        return make_response(response,200)
    if request.method=='POST':    
        data = request.get_json()
        new_user = User(username = data['username'], address=data['address'])
        db.session.add(new_user)
        db.session.commit()
        
        return make_response({"message":"Success"}, 200)
        
    
        
@app.route('/posts/<int:id>',methods = ['DELETE','PATCH','GET'])
def posts():
    # posts = Post.query.all()
    response = [post.to_dict() for post in Post.query.all()]
    
    return make_response(response, 200)
    

@app.route('/')
def index():
    return 'Welcome to flask'

if __name__ == '__main__':
    app.run(port=8000, debug=True)
