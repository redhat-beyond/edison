from edison import db


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
