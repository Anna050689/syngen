"""
This module provides the Context class and related functions for managing configuration context.

Classes:
--------
Context
    A class to manage configuration context.

Functions:
----------
get_context()
    Retrieves the singleton instance of Context.

global_context(metadata: Dict)
    Sets the global configuration context with the provided metadata.
"""

from syngen.ml.context.context import Context, global_context, get_context  # noqa: F401
