from typing import Dict
import copy


class Context:
    """
    A class used to represent the configuration context.

    Attributes
    ----------
    config : dict
        a dictionary to store configuration settings
    """

    def __init__(self):
        """
        Initializes the Context with an empty configuration.
        """
        self.config = {}

    def set_config(self, value: Dict):
        """
        Sets the configuration to a deep copy of the provided dictionary.

        Parameters
        ----------
        value : dict
            A dictionary containing configuration settings.
        """
        self.config = copy.deepcopy(value)

    def get_config(self) -> Dict:
        """
        Retrieves the current configuration.

        Returns
        -------
        dict
            The current configuration settings.
        """
        return self.config


# Singleton pattern to ensure there is only one instance of Configuration
_config_instance: Context = None


def get_context() -> Context:
    """
    Retrieves the singleton instance of the Context.

    Returns
    -------
    Context
        The singleton instance of the Context.
    """
    global _config_instance
    if _config_instance is None:
        _config_instance = Context()
    return _config_instance


def global_context(metadata: Dict):
    """
    Sets the global configuration context with the provided metadata.

    Parameters
    ----------
    metadata : dict
        A dictionary containing metadata to set as the global configuration.
    """
    global_config = get_context()
    global_config.set_config(metadata)
