import secrets
import importlib, inspect
import sys, inspect

config_dict = {}

# If config_dict is empty this function builds it dynamically 
# and returns the appropriate config object path.
def get_config_object(env_keyword: str):
    if(len(config_dict) == 0):
        # Iterating through all config.py members
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            # We're interested only with the derived classes of the Config class
            if inspect.isclass(obj) and name != "Config":
                config_dict[obj.ENV_KEYWORD] = ".".join([obj.__module__, name])
    
    return config_dict[env_keyword]
    
class Config:
    ENV_KEYWORD = ""
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

# PostgreSQL connection string should be updated once an actual production environment is established.
class ProductionConfig(Config):
    ENV_KEYWORD = "production"

class DevelopmentConfig(Config):
    ENV_KEYWORD = "development"
    DEBUG = True
