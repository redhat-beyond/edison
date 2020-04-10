from backend import db

class Token(db.Model):
    __tablename__ = 'token_blacklist'

    jti = db.Column(db.String(150), primary_key = True)
    creation_timestamp = db.Column(db.TIMESTAMP(timezone = False), nullable = False)

    def __init__(self, jti, creation_timestamp):
        self.jti = jti
        self.creation_timestamp = creation_timestamp
