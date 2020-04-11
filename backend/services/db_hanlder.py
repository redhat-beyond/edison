from backend import db
from models.token import Token
from datetime import datetime


class DBHandler:

    @staticmethod
    def get_by_id(model, _id):
        return model.query.get(_id)

    @staticmethod
    def get_all(model):
        return model.query.all()

    @staticmethod
    def add(model):
        db.session.add(model)
        db.session.commit()

    @staticmethod
    def delete(model):
        db.session.delete(model)
        db.session.commit()

    @staticmethod
    def update_user(updated_user, _id):
        user_to_be_updated = DBHandler.get_by_id(_id)
        if user_to_be_updated is None:
            raise ValueError(f"The user with id: {_id} is not in the DB.")

        user_to_be_updated.username = updated_user.username
        user_to_be_updated.first_name = updated_user.first_name
        user_to_be_updated.last_name = updated_user.last_name
        user_to_be_updated.password = updated_user.password
        user_to_be_updated.email = updated_user.email
        db.session.commit()

        return {'message': f'The user with id: {_id} was successfully updated'}

    @staticmethod
    def add_blacklisted_jti(jti):
        blacklisted_token = Token(jti, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        db.session.add(blacklisted_token)
        db.session.commit()

    @staticmethod
    def is_jti_blacklisted(jti):
        return Token.query.get(jti) is not None
