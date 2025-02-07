from typing import Dict
import copy


class Context:
    """
    A class to manage configuration settings using a dictionary.
    """
    def __init__(self):
        """
        Initializes a new instance of the Context class with an empty configuration.
        """
        self.config = {}

    def set_config(self, value: Dict):
        """
        Sets the configuration dictionary to a deep copy of the provided value.

        :param value: A dictionary containing configuration settings.
        """
        self.config = copy.deepcopy(value)

    def get_config(self) -> Dict:
        """
        Retrieves the current configuration dictionary.

        :return: A dictionary containing the current configuration settings.
        """
        return self.config


# Singleton pattern to ensure there is only one instance of Configuration
_config_instance: Context = None


def get_context() -> Context:
    """
    Retrieves the singleton instance of the Context class.

    :return: The singleton instance of the Context class.
    """
    global _config_instance
    if _config_instance is None:
        _config_instance = Context()
    return _config_instance


def global_context(metadata: Dict):
    """
    Sets the global configuration using the provided metadata.

    :param metadata: A dictionary containing metadata to set as the global configuration.
    """
    global_config = get_context()
    global_config.set_config(metadata)
