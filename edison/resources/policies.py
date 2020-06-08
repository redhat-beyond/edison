from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
import edison.models as models


class Policies(Resource):

    @jwt_required
    def get(self):
        status = 200
        current_user = models.User.query.filter_by(username=get_jwt_identity()).first()
        response = list(
            map(
                lambda policy: policy.to_json(), models.Policy.query.filter_by(user_id=current_user.id)
            )
        )

        return response, status
