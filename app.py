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
    # users = User.query.all()
    if request.method=='POST':
        response = [user.to_dict() for user in User.query.all()]
        
        data = request.get_json()
        
    
        return make_response(response,200)
@app.route('/posts',methods = ['POST','GET'])
def posts():
    # posts = Post.query.all()
    response = [post.to_dict() for post in Post.query.all()]
    
    return make_response(response, 200)
    

@app.route('/')
def index():
    return 'Welcome to flask'

if __name__ == '__main__':
    app.run(port=8000, debug=True)
