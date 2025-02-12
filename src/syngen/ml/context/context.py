from typing import Dict
import copy


class Context:
    """
    A class to manage configuration context using a singleton pattern.

    Attributes
    ----------
    config : dict
        A dictionary to store configuration settings.
    """
    def __init__(self):
        """Initialize the Context with an empty configuration dictionary."""
        self.config = {}

    def set_config(self, value: Dict):
        """
        Set the configuration dictionary.

        Parameters
        ----------
        value : dict
            The configuration settings to be stored.
        """
        self.config = copy.deepcopy(value)

    def get_config(self) -> Dict:
        """
        Get the configuration dictionary.

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
    Retrieve the singleton instance of Context.

    Returns
    -------
    Context
        The singleton instance of Context.
    """
    global _config_instance
    if _config_instance is None:
        _config_instance = Context()
    return _config_instance


def global_context(metadata: Dict):
    """
    Set the global configuration context.

    Parameters
    ----------
    metadata : dict
        The configuration settings to be applied globally.
    """
    global_config = get_context()
    global_config.set_config(metadata)
