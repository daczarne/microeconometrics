import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Instanciate the app
app = Flask(__name__)


## Configuration ##

# Can also be set as environment variables at the command line when deploying.
# export SECRET_KEY=mysecret
# set SECRET_KEY=mysecret
app.config["SECRET_KEY"] = "mysecret"


## DB set up ##

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app,db)


## Login Configs ##

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"


## Blueprint Configs ##

from puppycompanyblog.core.views import core
from puppycompanyblog.users.views import users
from puppycompanyblog.blog_posts.views import blog_posts
from puppycompanyblog.error_pages.handlers import error_pages

# Register the apps
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(core)
app.register_blueprint(error_pages)
