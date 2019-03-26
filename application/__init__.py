from flask import Flask
from unittest.test.testmock.testpatch import function
from distutils.command.config import config
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE:URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///items.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

#toiminnallisuus
from application import views

from application.items import models
from application.items import views

from application.auth import models
from application.auth import views

#kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
  
  #tietokantataulut
db.create_all()