import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from edison.config import get_config_object


# Put app here so the entire app could import it.
app = Flask(__name__)
app.config.from_object(get_config_object(app.config["ENV"]))
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy(app)
