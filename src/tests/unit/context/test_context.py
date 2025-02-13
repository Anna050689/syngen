import pytest
from src.syngen.ml.context.context import Context, get_context, global_context

### Positive Unit Tests for `Context` Class and Functions

#### Class: `Context`

def test_context_initialization():
    """Test that a new Context instance initializes with an empty configuration."""
    context = Context()
    assert context.get_config() == {}

def test_set_config():
    """Test that set_config correctly sets the configuration."""
    context = Context()
    config_data = {'key1': 'value1', 'key2': 'value2'}
    context.set_config(config_data)
    assert context.get_config() == config_data

#### Function: `get_context`

def test_get_context_singleton():
    """Test that get_context returns the same instance of Context."""
    context1 = get_context()
    context2 = get_context()
    assert context1 is context2

#### Function: `global_context`

def test_global_context():
    """Test that global_context sets the global configuration."""
    metadata = {'global_key': 'global_value'}
    global_context(metadata)
    context = get_context()
    assert context.get_config() == metadata

### Negative and Edge Unit Tests for `Context` Class and Functions

#### Class: `Context`

def test_get_config_without_setting():
    """Test that get_config handles the scenario where the configuration has not been set yet."""
    context = Context()
    assert context.get_config() == {}

def test_set_config_with_large_data():
    """Test that set_config can handle setting a large configuration dictionary."""
    context = Context()
    large_config = {f'key{i}': f'value{i}' for i in range(1000)}
    context.set_config(large_config)
    assert context.get_config() == large_config

def test_set_config_with_nested_dictionary():
    """Test that set_config correctly handles a deeply nested dictionary."""
    context = Context()
    nested_config = {
        'level1': {
            'level2': {
                'level3': {
                    'level4': {
                        'level5': 'deep_value'
                    }
                }
            }
        }
    }
    context.set_config(nested_config)
    assert context.get_config() == nested_config

#### Function: `get_context`

def test_get_context_singleton_with_modification():
    """Test that modifying one instance of Context affects the instance returned by get_context."""
    context1 = get_context()
    context1.set_config({'modified_key': 'modified_value'})
    context2 = get_context()
    assert context2.get_config() == {'modified_key': 'modified_value'}

def test_get_context_multiple_calls_consistency():
    """Ensure that multiple consecutive calls to get_context return the same instance."""
    context1 = get_context()
    context2 = get_context()
    assert context1 is context2
