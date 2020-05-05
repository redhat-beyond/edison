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

    def get(self, policy_name: str, username: str):
        policy = models.Policy.query.filter_by(name=policy_name).first()
        # TODO - get the policy in name 'policy_name' of the user that asking for it
        if policy:
            status = 200
            response = {'policy': policy.to_json()}
        else:
            status = 404
            response = {'msg': f"user {username} doesnt have policy name {policy_name}"}

        return response, status

    def delete(self, policy_name: str, username: str):
        response = {'msg': 'Policy deleted'}
        status = 200

        if self.__request_is_legal(username):
            db.session.delete(models.Policy.query.filter_by(name=policy_name).first())
            db.session.commit()

        else:
            response = {'msg': 'Policy can be deleted just by the policy owner'}
            status = 403

        return response, status

    def __request_is_legal(self, username: str):
        return get_jwt_identity() == username
