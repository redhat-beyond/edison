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

class ProductionConfig(Config):
    ENV_KEYWORD = "production"

class DevelopmentConfig(Config):
    ENV_KEYWORD = "development"
    DEBUG = True
