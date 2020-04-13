from abc import ABC, abstractmethod
from backend import db


class BaseStorageHandler(ABC):

    @abstractmethod
    def get_by_username(self, model: db.Model, username: str):
        pass

    @abstractmethod
    def get_by_id(self, model: db.Model, _id: int):
        pass

    @abstractmethod
    def get_all(self, model: db.Model):
        pass

    @abstractmethod
    def add(self, model: db.Model):
        pass

    @abstractmethod
    def delete(self, model: db.Model):
        pass

    @abstractmethod
    def update_user(self, updated_user: db.Model, username: str):
        pass

    @abstractmethod
    def add_blacklisted_jti(self, jti: str):
        pass

    @abstractmethod
    def is_jti_blacklisted(self, jti: str):
        pass
