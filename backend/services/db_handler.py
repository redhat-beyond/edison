from backend import db
from datetime import datetime
from .base_storage_handler import BaseStorageHandler
import backend.models as models


class DBHandler(BaseStorageHandler):

    def get_by_username(self, model: db.Model, username: str):
        return model.query.filter_by(username=username).first()

    def get_by_id(self, model: db.Model, _id: int):
        return model.query.get(_id)

    def get_all(self, model: db.Model):
        return model.query.all()

    def add(self, model: db.Model):
        db.session.add(model)
        db.session.commit()

    def delete(self, model: db.Model):
        db.session.delete(model)
        db.session.commit()
    
    def update_user(self, updated_user: db.Model, username: str):
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

    def add_blacklisted_jti(self, jti: str):
        blacklisted_token = models.Token(jti, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        db.session.add(blacklisted_token)
        db.session.commit()

    def is_jti_blacklisted(self, jti: str):
        return models.Token.query.get(jti) is not None
