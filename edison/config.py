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
