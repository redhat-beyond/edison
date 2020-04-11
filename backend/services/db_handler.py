from backend import db
from datetime import datetime
import backend.models as models

class DBHandler:

    @staticmethod
    def get_by_username(model, username):
        return model.query.filter_by(username = username).first()

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
    def update_user(updated_user, username):
        user_to_be_updated = DBHandler.get_by_username(models.User, username)
        if user_to_be_updated is None:
            raise ValueError(f"The user with username: {username} is not in the DB.")

        user_to_be_updated.username = updated_user.username
        user_to_be_updated.first_name = updated_user.first_name
        user_to_be_updated.last_name = updated_user.last_name
        user_to_be_updated.password = updated_user.password
        user_to_be_updated.email = updated_user.email
        db.session.commit()

        return user_to_be_updated

    @staticmethod
    def add_blacklisted_jti(jti):
        blacklisted_token = models.Token(jti, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        db.session.add(blacklisted_token)
        db.session.commit()

    @staticmethod
    def is_jti_blacklisted(jti):
        return models.Token.query.get(jti) is not None
