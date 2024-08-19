from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

# application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  
application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'

# DBVAR = 'postgresql://postgres:7714LLUVIa!@awseb-e-ur4b2ayayc-stack-awsebrdsdatabase-9wo12f792ayt.cmabmb6a49ok.us-east-1.rds.amazonaws.com:5432/ebdb'
# application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
# application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

DBVAR = 'sqlite:///user.db'
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR
application.config['SQLALCHEMY_BINDS'] ={'sentence': 'sqlite:///sentence_table.db'}


db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.business.routes import business
from capp.light_talk_app.routes import light_talk_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(business)
application.register_blueprint(light_talk_app)
application.register_blueprint(users)

