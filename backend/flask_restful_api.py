from flask_restful import Api
from flask_jwt_extended import JWTManager
import backend


# API description in swagger - https://app.swaggerhub.com/apis/DoRTaL94/UserManagment/1.0.0

app = backend.app
# Creates all tables in app. Table's name defined with __tablename__ variable.
backend.db.create_all()
api = Api(app)
# Creation of Json-Web-Token manager.
# In order to reach secured endpoints client should add an authorization header with the value Bearer <token>.
jwt = JWTManager(app)
