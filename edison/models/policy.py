from edison import db
from flask_restful import reqparse


class Policy(db.Model):
    _tablename_ = 'policy'
    _table_args_ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    policy_name = db.Column(db.String(50), nullable=False)
    room = db.Column(db.String(50), nullable=False)
    conditions = db.Column(db.String(300), nullable=False)
    commands = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "policy_name": self.policy_name,
            "room": self.room,
            "conditions": self.conditions,
            "commands": self.commands
        }

    def __repr__(self):
        return f"<Policy: id = {self.policy_name}, title = {self.room}, " \
           f"sensors= {self.conditions}, username = {self.commands}>"

    @staticmethod
    def create_parser():
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

        return parser

