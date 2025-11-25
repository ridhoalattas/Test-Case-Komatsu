import os

import yaml

from config.config_model import (
    Config as ConfigModel,
)


class Config:
    def load(self):
        """
        Load the configuration

        Returns:
            ConfigModel: The loaded configuration.

        """

        try:
            config_path = os.path.join(os.path.dirname(__file__), "config.yaml")

            with open(config_path, "r") as file:
                config = yaml.safe_load(file)

            cfg = ConfigModel(**config)
            return cfg

        except Exception as e:
            raise e
