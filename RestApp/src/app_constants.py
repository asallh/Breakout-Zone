import configparser
import os


class Constants:

    config = configparser.ConfigParser

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

    @classmethod
    def get_mongo_username(cls):
       return os.getenv("mongodb_username", cls.config[cls.get_environment()]["mongodb_username"])

    @classmethod
    def get_mongo_password(cls):
        env_mongo_password = os.getenv('MONGO_PASSWORD')
        if env_mongo_password is None:
            raise EnvironmentError("Environment variable MONGO_PASSWORD not found")
        return env_mongo_password