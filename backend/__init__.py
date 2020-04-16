from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


db_role = 'postgres'
db_password = 'edison'
db_url = '0.0.0.0'
db_name = 'edison'

# Put app and db here so the entire app could import them.
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}/{}'.format(db_role, db_password, db_url, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
