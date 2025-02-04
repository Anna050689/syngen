from typing import Dict
import copy


class Context:
    """
    Manages configuration settings using a dictionary.
    
    Attributes
    ----------
    config : dict
        A dictionary to store configuration settings.
    
    Methods
    -------
    set_config(value: Dict)
        Sets the configuration dictionary to a deep copy of the provided value.
    get_config() -> Dict
        Retrieves the current configuration dictionary.
    """
    
    def __init__(self):
        """
        Initializes a new instance of the Context class with an empty configuration.
        """
        self.config = {}

    def set_config(self, value: Dict):
        """
        Sets the configuration dictionary to a deep copy of the provided value.
        
        Parameters
        ----------
        value : Dict
            The configuration dictionary to be set.
        """
        self.config = copy.deepcopy(value)

    def get_config(self) -> Dict:
        """
        Retrieves the current configuration dictionary.
        
        Returns
        -------
        Dict
            The current configuration dictionary.
        """
        return self.config


# Singleton pattern to ensure there is only one instance of Configuration
_config_instance: Context = None


def get_context() -> Context:
    """
    Retrieves the singleton instance of the Context class, creating it if necessary.
    
    Returns
    -------
    Context
        The singleton instance of the Context class.
    """
    global _config_instance
    if _config_instance is None:
        _config_instance = Context()
    return _config_instance


def global_context(metadata: Dict):
    """
    Sets the global configuration using the provided metadata dictionary.
    
    Parameters
    ----------
    metadata : Dict
        The metadata dictionary to set as the global configuration.
    """
    global_config = get_context()
    global_config.set_config(metadata)
