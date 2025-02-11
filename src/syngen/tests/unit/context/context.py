import pytest
from src/syngen.ml.context.context import Context, get_context, global_context

def test_context_initialization():
    context = Context()
    assert context.get_config() == {}

def test_context_set_config():
    context = Context()
    config_data = {'key1': 'value1', 'key2': 'value2'}
    context.set_config(config_data)
    assert context.get_config() == config_data

def test_context_get_config():
    context = Context()
    config_data = {'key1': 'value1'}
    context.set_config(config_data)
    assert context.get_config() == config_data

def test_get_context_singleton():
    context1 = get_context()
    context2 = get_context()
    assert context1 is context2

def test_global_context_setting():
    metadata = {'global_key': 'global_value'}
    global_context(metadata)
    context = get_context()
    assert context.get_config() == metadata

def test_context_get_config_without_setting():
    context = Context()
    assert context.get_config() == {}

def test_get_context_singleton_integrity():
    global _config_instance
    _config_instance = None  # Manually alter the instance
    context = get_context()
    assert isinstance(context, Context)

def test_context_set_config_large_dict():
    context = Context()
    large_config = {f'key{i}': f'value{i}' for i in range(1000)}
    context.set_config(large_config)
    assert context.get_config() == large_config

def test_context_set_config_nested_dict():
    context = Context()
    nested_config = {
        'level1': {
            'level2': {
                'level3': {
                    'key': 'value'
                }
            }
        }
    }
    context.set_config(nested_config)
    assert context.get_config() == nested_config

def test_get_context_multiple_calls():
    context1 = get_context()
    context2 = get_context()
    context3 = get_context()
    assert context1 is context2 is context3

def test_global_context_with_empty_metadata():
    global_context({})
    context = get_context()
    assert context.get_config() == {}