from flask import Flask, make_response
from flask_migrate import Migrate
from models import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///recap.db"

# Initialize the database with the app
migrate = Migrate(app, db)
db.init_app(app)

# Initialize Flask-Migrate with the app and db
@app.route('/users')
def users():
    users = User.query.all()
    response = [user.to_dict() for user in User.query.all()]
    
    return make_response(response,200)
@app.route('/')
def index():
    return 'Welcome to flask'

if __name__ == '__main__':
    app.run(port=8000, debug=True)
