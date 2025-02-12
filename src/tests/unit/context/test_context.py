import pytest
from src.syngen.ml.context.context import Context

def test_initialization():
    context = Context()
    assert context.get_config() == {}, "Initialization failed, config should be empty."

def test_set_config():
    context = Context()
    config_data = {'key1': 'value1', 'key2': 'value2'}
    context.set_config(config_data)
    assert context.get_config() == config_data, "Set config failed, config does not match."

def test_set_config_deep_copy():
    context = Context()
    config_data = {'key1': 'value1', 'key2': 'value2'}
    context.set_config(config_data)
    config_data['key1'] = 'new_value'
    assert context.get_config() != config_data, "Deep copy failed, config should not change."

def test_get_config():
    context = Context()
    config_data = {'key1': 'value1', 'key2': 'value2'}
    context.set_config(config_data)
    assert context.get_config() == config_data, "Get config failed, config does not match."

def test_set_config_large_dictionary():
    context = Context()
    large_config = {f'key{i}': f'value{i}' for i in range(1000)}
    context.set_config(large_config)
    assert context.get_config() == large_config, "Set config with large dictionary failed, config does not match."

def test_set_config_nested_dictionary():
    context = Context()
    nested_config = {
        'key1': {
            'subkey1': {
                'subsubkey1': 'value1'
            }
        },
        'key2': {
            'subkey2': {
                'subsubkey2': 'value2'
            }
        }
    }
    context.set_config(nested_config)
    assert context.get_config() == nested_config, "Set config with nested dictionary failed, config does not match."
