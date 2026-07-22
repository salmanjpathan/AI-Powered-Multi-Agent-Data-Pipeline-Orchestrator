import json
import os


class Settings:

    def __init__(self):

        config_path = os.path.join(
            os.path.dirname(__file__),
            "config.json"
        )

        with open(config_path, "r") as file:
            self.config = json.load(file)

    @property
    def raw_path(self):
        return self.config["paths"]["raw"]

    @property
    def bronze_path(self):
        return self.config["paths"]["bronze"]

    @property
    def silver_path(self):
        return self.config["paths"]["silver"]

    @property
    def gold_path(self):
        return self.config["paths"]["gold"]

    @property
    def logs_path(self):
        return self.config["paths"]["logs"]

    @property
    def ollama_model(self):
        return self.config["ollama"]["model"]


settings = Settings()