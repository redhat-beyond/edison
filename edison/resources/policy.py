
from flask_jwt_extended import jwt_required, get_jwt_identity
from edison import db, app
import edison.models as models

from flask_restful import Resource, reqparse
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError


class Policy(Resource):
    # RequestParser enforces arguments in requests.
    # If one of the arguments not exists, client gets an error response.
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True
    )
    parser.add_argument(
        'room',
        type=str,
        required=True
    )
    parser.add_argument(
        'conditions',
        type=str,
        required=True
    )
    parser.add_argument(
        'commands',
        type=str,
        required=True
    )

    @jwt_required
    def post(self, username: str):
        data = Policy.parser.parse_args()
        status = 200
        response = {}

        if self.__request_is_legal(username):
            try:
                db.session.add(models.Policy(**data))
                db.session.commit()

                response = {'msg': 'policy added successfully'}

            except KeyError:
                response = {'msg': 'Update failed. Json missing keys.'}
                status = 400

            except IntegrityError as e:
                status = 400
                if isinstance(e.orig, UniqueViolation):
                    response = {'msg': 'Policy name is taken.'}
                else:
                    response = {'msg': 'Unknown error.'}
        else:
            status = 403
            response = {'msg': 'User can only add policy to himself'}

        return response, status

    def __request_is_legal(self, username: str):
        return get_jwt_identity() == username
