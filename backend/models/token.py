from backend import db


class Token(db.Model):
    __tablename__ = 'token_blacklist'

    jti = db.Column(db.String(150), primary_key=True)
    creation_timestamp = db.Column(db.TIMESTAMP(timezone=False), nullable=False)

    def __repr__(self):
        return f"<Token: jti: {self.jti}, creation time: {self.creation_timestamp}."
