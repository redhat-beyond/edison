import edison.models as models

from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token)
from passlib.hash import pbkdf2_sha256 as sha256


class Login(Resource):
    # RequestParser enforces arguments in requests. 
    # If one of the arguments not exists, client gets an error response.
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True
    )
    parser.add_argument(
        'password',
        type=str,
        required=True
    )

    def post(self):
        data = Login.parser.parse_args()
        username = data['username']
        current_user = models.User.query.filter_by(username=username).first()
        status = 200
        response = {}

        if not current_user:
            response = {'msg': 'Username or password is incorrect'}
            status = 401

        else:
            if sha256.verify(data['password'], current_user.password):
                access_token = create_access_token(identity = data['username'])
                refresh_token = create_refresh_token(identity = data['username'])

                response = {
                    'msg': 'Logged in as {}'.format(current_user.username),
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
            else:
                response = {'msg': 'Username or password is incorrect'}
                status = 401
        
        return response, status
