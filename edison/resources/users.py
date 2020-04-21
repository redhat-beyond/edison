from flask_restful import Resource
from flask_jwt_extended import jwt_required
import edison.models as models


class Users(Resource):

    @jwt_required
    def get(self):
        status = 200
        response = list(
            map(
                lambda user: user.to_json(), models.User.query.all()
            )
        )

        return response, status
