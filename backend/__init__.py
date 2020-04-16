from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


# Put app and db here so the entire app could import them.
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:edison@127.0.0.1/edison'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
