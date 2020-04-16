from abc import ABC, abstractmethod
from backend import db
from typing import Dict

class BaseStorageHandler(ABC):

    @abstractmethod
    def get_by_filters(self, model: db.Model, filters: Dict[str, str]):
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
    def update(self):
        pass
