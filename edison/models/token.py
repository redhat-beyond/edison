from edison import db


class Token(db.Model):
    __tablename__ = 'token_blacklist'

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(150), nullable=False, unique=True)
    creation_timestamp = db.Column(db.TIMESTAMP(timezone=False), nullable=False)

    def __repr__(self):
        return f"<Token: jti: {self.jti}, creation time: {self.creation_timestamp}>"
