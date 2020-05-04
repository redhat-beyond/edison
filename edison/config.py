import inspect
import sys


def get_config_object(env_keyword: str):
    """
    Returns the wanted environment details to configure the app

    the function iterate on a dictionary which is build by inspect.
    the dictionary has key - name, and value - obj.
    name is for the name of class/ function etc. in the wanted module
    obj is for the content itself
    we return the configuration details of the class that inherit from class Config
    and that its ENV_KEYWORD field is the same as env_keyword parameter

    Parameters:
    env_keyword (str): the keyword that represent the wanted environment to be configured

    Returns:
    str: module_name.class_name, the position of the wanted configuration class
    """

    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(Config) and obj.ENV_KEYWORD == env_keyword:
            return ".".join([obj.__module__, name])


class Config:
    ENV_KEYWORD = ""
    DEBUG = False


class ProductionConfig(Config):
    ENV_KEYWORD = "production"


class DevelopmentConfig(Config):
    ENV_KEYWORD = "development"
    DEBUG = True
