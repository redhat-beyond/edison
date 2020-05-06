from edison import db
import json

# TODO - make the policy id and the user_id a unique combination


class Policy(db.Model):
    _tablename_ = 'policy'
    _table_args_ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    policy_name = db.Column(db.String(50), nullable=False, unique=True)
    room = db.Column(db.String(50), nullable=False)
    conditions = db.Column(db.String(300), nullable=False)
    commands = db.Column(db.String(300), nullable=False)
    user_id = db.column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_json(self):
        return {
            "policy_name": self.policy_name,
            "room": self.room,
            "conditions": self.conditions,
            "commands": self.commands
        }

      #  return json.dumps(self, defualt=lambda obj: obj.__dict__, sort_keys=True, indent=4)

    def _repr_(self):
        return f"<Policy: id = {self.policy_name}, title = {self.room}, " \
           f"sensors= {self.conditions}, username = {self.commands}>"
