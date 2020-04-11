from backend import db


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    password = db.Column(db.String(150), nullable = False)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(150), nullable = False)
    
    def __repr__(self):
        return f"<User: id = {self.id}, first_name = {self.first_name}, " \
               f"last_name = {self.last_name}, username = {self.username}, email = {self.email}>"
