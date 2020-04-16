import secrets


class Config(object):
    DEBUG = False
    # Turn off the Flask-SQLAlchemy event system
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Enables response message for unauthenticated requests
    PROPAGATE_EXCEPTIONS = True
    # This tells the JWTManager to use jwt.token_in_blacklist_loader callback
    JWT_BLACKLIST_ENABLED = True
    # JWTManager uses this secret key for creating tokens
    JWT_SECRET_KEY = secrets.token_hex(24)
    # We're going to check if both access_token and refresh_token are black listed
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:edison@127.0.0.1/edison'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
