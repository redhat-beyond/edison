from flask_restful import Api
from flask_jwt_extended import JWTManager
import secrets
import backend

# API description in swagger - https://app.swaggerhub.com/apis/DoRTaL94/UserManagment/1.0.0

app = backend.app
# Creates all tables in app. Table's name defined with __tablename__ variable.
backend.db.create_all()
# Enables response message for unauthenticated requests
app.config['PROPAGATE_EXCEPTIONS'] = True
# JWTManager uses this secret key for creating tokens
app.config['JWT_SECRET_KEY'] = secrets.token_hex(24)
# This tells the JWTManager to call 'check_if_token_in_blacklist' function below on every request
app.config['JWT_BLACKLIST_ENABLED'] = True
# We're going to check if both access_token and refresh_token are black listed
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
api = Api(app)
# Creation of Json-Web-Token manager.
# In order to reach secured endpoints client should add an authorization header with the value Bearer <token>.
jwt = JWTManager(app)
