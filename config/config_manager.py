import yaml
import os

class ConfigManager:

    @staticmethod
    def get_config():

        env = os.getenv("ENV", "qa")

        with open("config/config.yaml") as file:
            data = yaml.safe_load(file)

        return data["environments"][env]