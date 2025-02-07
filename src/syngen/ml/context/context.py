from typing import Dict
import copy


class Context:
    """A class to manage configuration settings."""

    def __init__(self):
        """Initialize the Context with an empty configuration."""
        self.config = {}

    def set_config(self, value: Dict):
        """Set the configuration using a deep copy of the provided dictionary.

        Args:
            value (Dict): The configuration dictionary to set.
        """
        self.config = copy.deepcopy(value)

    def get_config(self) -> Dict:
        """Get the current configuration.

        Returns:
            Dict: The current configuration dictionary.
        """
        return self.config


# Singleton pattern to ensure there is only one instance of Configuration
_config_instance: Context = None


def get_context() -> Context:
    """Get the singleton instance of Context.

    Returns:
        Context: The singleton instance of Context.
    """
    global _config_instance
    if _config_instance is None:
        _config_instance = Context()
    return _config_instance


def global_context(metadata: Dict):
    """Set the global configuration context.

    Args:
        metadata (Dict): The metadata to set as the global configuration.
    """
    global_config = get_context()
    global_config.set_config(metadata)
