import edison
from flask import render_template
from flask_restful import Api
from flask_jwt_extended import JWTManager
from edison.resources import *
import edison.models as models


# API description in swagger - https://app.swaggerhub.com/apis/DoRTaL94/UserManagment/1.0.0

app = edison.app
# Creates all tables in app. Table's name defined with __tablename__ variable.
edison.db.create_all()
api = Api(app)
# Creation of Json-Web-Token manager.
# In order to reach secured endpoints client should add an authorization header with the value Bearer <token>.
jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    filters = {'jti': jti}
    return models.Token.query.filter_by(**filters).first() is not None


@app.route("/")
def index():
	return render_template('index.html')

api.add_resource(Users, '/api/users')
