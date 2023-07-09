from os.path import exists
from yaml import safe_load
from typing import Dict

class ReadConfiguration:
    """Class for reading configuration from a YAML file."""

    def __init__(self, config_file_path: str) -> None:
        """Initialize ReadConfiguration class.

        Args:
            config_file_path (str): Path to the configuration file.
        """
        self.config_path = config_file_path

    def readConfig(self) -> Dict:
        """Reads the configuration from the YAML file.

        Returns:
            dict: Configuration data.
        Raises:
            Exception: If the configuration file is not found at the specified path.
        """
        if exists(self.config_path):
            with open(self.config_path) as file:
                config = safe_load(file)
        else:
            raise FileNotFoundError(f"Configuration file not found at the specified path: {self.config_path}")
        
        return config
