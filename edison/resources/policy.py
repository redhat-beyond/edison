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

    def get(self, policy_name: str):
        policy = models.Policy.query.filter_by(name=policy_name).first()

        status = 200 if policy else 404
        response = {
                 policy: policy.to_json()
        } if policy else {'msg': 'policy not found'}

        return response, status
