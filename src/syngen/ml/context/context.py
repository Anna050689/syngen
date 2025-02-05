from typing import Dict
import copy


class Context:
    """
    A class to manage configuration context using a singleton pattern.
    """
    def __init__(self):
        """
        Initialize the Context with an empty configuration.
        """
        self.config = {}

    def set_config(self, value: Dict):
        """
        Set the configuration with a deep copy of the provided dictionary.

        :param value: A dictionary containing configuration settings.
        """
        self.config = copy.deepcopy(value)

    def get_config(self) -> Dict:
        """
        Retrieve the current configuration.

        :return: A dictionary containing the current configuration settings.
        """
        return self.config


# Singleton pattern to ensure there is only one instance of Configuration
_config_instance: Context = None


def get_context() -> Context:
    """
    Retrieve the singleton instance of Context.

    :return: The singleton Context instance.
    """
    global _config_instance
    if _config_instance is None:
        _config_instance = Context()
    return _config_instance


def global_context(metadata: Dict):
    """
    Set the global configuration context with the provided metadata.

    :param metadata: A dictionary containing metadata to set as global configuration.
    """
    global_config = get_context()
    global_config.set_config(metadata)
