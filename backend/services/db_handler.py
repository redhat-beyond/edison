from backend import db
from datetime import datetime
from backend.services.base_storage_handler import BaseStorageHandler
from typing import Dict


class DBHandler(BaseStorageHandler):

    def get_by_filters(self, model: db.Model, filters: Dict[str, str]):
        return model.query.filter_by(**filters).first()

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
    
    def update(self):
        db.session.commit()
