from backend.models.user import User

# This class should be used for sending users information to client.
# We don't want to send sensitive information such as password or email.
class ResponseUser:
    def __init__(self, user: User):
        self.id = user.id
        self.username = user.username
        self.first_name = user.first_name
        self.last_name = user.last_name
