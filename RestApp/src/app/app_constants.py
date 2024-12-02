import configparser
import os


class Constants:

    LOGGER_DEFAULT = "NHL API LOGGER"
    config = configparser.ConfigParser

    @classmethod
    def get_mongo_instance(cls):
        return cls.get_mongo_host() + ":" + cls.get_mongo_port()

    @classmethod
    def get_environment(cls):
        environment = os.getenv("ENVIRONMENT")
        if environment is None:
            raise EnvironmentError("Environment variable not set")
        return environment

    @classmethod
    def get_mongo_host(cls):
       return os.getenv("mongodb_host", cls.config[cls.get_environment()]["mongodb_host"])

    @classmethod
    def get_mongo_port(cls):
       return os.getenv("mongodb_port", cls.config[cls.get_environment()]["mongodb_port"])

    @classmethod
    def get_mongo_username(cls):
       return os.getenv("mongodb_username", cls.config[cls.get_environment()]["mongodb_username"])

    @classmethod
    def get_mongo_database(cls):
       return (os.getenv("mongodb_database", cls.config[cls.get_environment()]["mongodb_database"])

    @classmethod)
    def get_mongo_attributes(cls):
       return os.getenv("mongodb_attributes", cls.config[cls.get_environment()]["mongodb_attributes"])

    @classmethod
    def get_mongo_password(cls):
        env_mongo_password = os.getenv('MONGO_PASSWORD')
        if env_mongo_password is None:
            raise EnvironmentError("Environment variable MONGO_PASSWORD not found")
        return env_mongo_password