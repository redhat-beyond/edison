from flask_jwt_extended import jwt_required, get_jwt_identity
from edison import db, app
import edison.models as models

from flask_restful import Resource, reqparse


class Policy(Resource):
    # RequestParser enforces arguments in requests.
    # If one of the arguments not exists, client gets an error response.
    parser = reqparse.RequestParser()
    parser.add_argument(
        'policy_name',
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
        policy = models.Policy.query.filter_by(policy_name=policy_name).first()
        current_user = models.User.query.filter_by(username=get_jwt_identity()).first()
        # filters = TODO - add filters by user id and policy name

        if models.Policy.query.filter_by(policy_name=policy_name).first() is not None:
            status = 200
            response = {'policy': policy.to_json()}
        else:
            status = 404
            response = {'msg': f"user doesnt have policy name {policy_name}"}

        return response, status

    def delete(self, policy_name: str):
        response = {'msg': 'Policy deleted successfully'}
        status = 200

        current_user = models.User.query.filter_by(username=get_jwt_identity()).first()
        # filters = TODO - add filters by user id and policy name

        if models.Policy.query.filter_by(policy_name=policy_name).first() is not None:
            db.session.delete(models.Policy.query.filter_by(policy_name=policy_name).first())
            db.session.commit()

        else:
            response = {'msg': f"user doesnt have policy name {policy_name}"}
            status = 400

        return response, status
