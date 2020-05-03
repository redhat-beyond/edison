import os

from flask import Flask


# Put app here so the entire app could import it.
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
