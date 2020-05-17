import inspect
import sys


def get_config_object(env_keyword: str):
    """
    Returns the the desired config class path.

    The function iterates through a dictionary returned by inspect.
    The dictionary contains details about all of the file members.
    Its key is the name of the member and value is obj which contains all the details about the member.
    The desired config path is being picked by the ENV_KEYWORD field defined in the config class.

    Parameters:
    env_keyword (str): Should be equals to one of the config classes ENV_KEYWORD field.

    Returns:
    str: module_name.class_name, which is the full path of the config class.
    """
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if issubclass(obj, Config) and obj.ENV_KEYWORD == env_keyword:
            return ".".join([obj.__module__, name])


class Config:
    ENV_KEYWORD = ""
    DEBUG = False
    # Turns off the Flask-SQLAlchemy event system
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:edison@127.0.0.1/edison'

# PostgreSQL connection string should be updated once an actual production environment is established.
class ProductionConfig(Config):
    ENV_KEYWORD = "production"


class DevelopmentConfig(Config):
    ENV_KEYWORD = "development"
    DEBUG = True
