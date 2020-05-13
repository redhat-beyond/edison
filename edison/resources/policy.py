from flask_jwt_extended import jwt_required, get_jwt_identity
from edison import db, app
import edison.models as models

from flask_restful import Resource


class Policy(Resource):

    parser = models.Policy.create_parser()

    @jwt_required
    def get(self, policy_name: str):

        current_user = models.User.query.filter_by(username=get_jwt_identity()).first()
        filters = {'policy_name': policy_name, 'user_id': current_user.id}

        policy = models.Policy.query.filter_by(**filters).first()

        if policy is not None:
            status = 200
            response = {'policy': policy.to_json()}
        else:
            status = 404
            response = {'msg': f"User {current_user.username} does'nt have policy name {policy_name}"}

        return response, status

    @jwt_required
    def delete(self, policy_name: str):

        current_user = models.User.query.filter_by(username=get_jwt_identity()).first()
        filters = {'policy_name': policy_name, 'user_id': current_user.id}

        policy_to_delete = models.Policy.query.filter_by(**filters).first()

        if policy_to_delete is not None:
            db.session.delete(policy_to_delete)
            db.session.commit()

            response = {'msg': f"Policy {policy_name} deleted successfully"}
            status = 200

        else:
            response = {'msg': f"User {current_user.username} does'nt have policy name {policy_name}"}
            status = 400

        return response, status

    @jwt_required
    def put(self, policy_name: str):

        updated_policy = Policy.parser.parse_args()
        current_user = models.User.query.filter_by(username=get_jwt_identity()).first()
        filters = {'policy_name': policy_name, 'user_id': current_user.id}

        policy_to_update = models.Policy.query.filter_by(**filters).first()

        if policy_to_update is not None:
            try:
                policy_to_update.policy_name = updated_policy['policy_name']
                policy_to_update.room = updated_policy['room']
                policy_to_update.conditions = updated_policy['conditions']
                policy_to_update.commands = updated_policy['commands']

                db.session.commit()
                response = {'msg': 'Policy updated', 'policy': policy_to_update.to_json()}
                status = 200

            except KeyError:
                response = {'msg': 'Update failed. Json missing keys.'}
                status = 400
        else:
            response = {'msg': f"User {current_user.username} does't have policy name {policy_name}"}
            status = 400

        return response, status
