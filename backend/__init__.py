from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


# Put app and db here so the entire app could import them.
app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("backend.config.ProductionConfig")
else:
    app.config.from_object("backend.config.DevelopmentConfig")
    
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy(app)
