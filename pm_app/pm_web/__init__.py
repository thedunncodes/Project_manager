from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DEV'
app.config['MONGODB_SETTINGS'] = {
    'db': 'project_management_db',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from .main import routes

