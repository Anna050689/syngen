from typing import Dict
import copy


class Context:
    """A class to manage configuration settings using a dictionary."""

    def __init__(self):
        """Initialize the Context with an empty configuration dictionary."""
        self.config = {}

    def set_config(self, value: Dict):
        """Set the configuration dictionary to a deep copy of the provided value.

        Args:
            value (Dict): The configuration settings to be stored.
        """
        self.config = copy.deepcopy(value)

    def get_config(self) -> Dict:
        """Retrieve the current configuration settings.

        Returns:
            Dict: The current configuration settings.
        """
        return self.config


# Singleton pattern to ensure there is only one instance of Configuration
_config_instance: Context = None


def get_context() -> Context:
    """Retrieve the singleton instance of the Context class.

    Returns:
        Context: The singleton instance of the Context class.
    """
    global _config_instance
    if _config_instance is None:
        _config_instance = Context()
    return _config_instance


def global_context(metadata: Dict):
    """Set the global configuration context with the provided metadata.

    Args:
        metadata (Dict): The metadata to set as the global configuration.
    """
    global_config = get_context()
    global_config.set_config(metadata)
