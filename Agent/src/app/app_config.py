import configparser
import os.path


class MissingEnvironmentVariableError(EnvironmentError):
    def __init__(self, env_var_name):
        self.message = f"Required environment varaible {env_var_name} is not set"
        super().__init__(self.message)

class Constants:
    config = configparser.ConfigParser()
    config_dir = os.path.dirname(os.path.realpath(__file__))
    ini_path = os.path.join(config_dir, "app.ini")
    config.read(ini_path)

    @classmethod
    def get_environment_variable(cls, env_var, required=True):
        env_var_value = os.getenv(env_var, cls.config.get(cls.get_environment(), env_var, fallback=None))
        if env_var_value is None and required is True:
            raise MissingEnvironmentVariableError(env_var)
        return env_var_value

    @classmethod
    def get_environment(cls):
        env = os.getenv("ENVIRONMENT")
        if not env:
            raise MissingEnvironmentVariableError("ENVIRONMENT")
        return env

    @classmethod
    def get_players_rest_endpoint(cls):
        return cls.get_environment_variable("local_rest_endpoint")