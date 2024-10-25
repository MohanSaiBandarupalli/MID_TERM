"""
This module contains additional unit tests to improve coverage for the PluginManager class.
It includes tests for error handling and edge cases.
"""

import pytest
from src.plugin_manager import PluginManager

# pylint: disable=redefined-outer-name

@pytest.fixture
def empty_plugin_manager():
    """Fixture to initialize an empty PluginManager instance for testing."""
    return PluginManager()

def test_register_none_plugin(empty_plugin_manager):
    """Test registering None as a plugin to ensure it raises a TypeError."""
    with pytest.raises(TypeError):
        empty_plugin_manager.register_plugin("none_plugin", None)

def test_get_nonexistent_plugin(empty_plugin_manager):
    """Test retrieving a plugin that hasn't been registered."""
    assert empty_plugin_manager.get_plugin("nonexistent") is None

def test_list_plugins_empty(empty_plugin_manager):
    """Test listing plugins when no plugins have been registered."""
    assert not list(empty_plugin_manager.list_plugins())  # Simplified boolean check

def test_load_plugins_from_empty_directory(empty_plugin_manager, tmp_path):
    """Test loading plugins from an empty directory."""
    empty_plugin_manager.load_plugins(str(tmp_path))
    assert not list(empty_plugin_manager.list_plugins())  # Simplified boolean check

def test_load_plugins_from_nonexistent_directory(empty_plugin_manager):
    """Test loading plugins from a non-existent directory."""
    non_existent_dir = "./non_existent_directory"
    with pytest.raises(FileNotFoundError):
        empty_plugin_manager.load_plugins(non_existent_dir)

def test_register_duplicate_plugin(empty_plugin_manager):
    """Test registering a plugin with a duplicate name."""
    class MockPlugin:
        """A mock plugin class for testing."""
        def execute(self):
            """Mock execute method."""
            return "Executed"

    empty_plugin_manager.register_plugin("mock", MockPlugin())
    # Register the same plugin name again and check it overwrites
    empty_plugin_manager.register_plugin("mock", MockPlugin())
    assert list(empty_plugin_manager.list_plugins()) == ["mock"]

def test_plugin_execute_method(empty_plugin_manager):
    """Test that a registered plugin's execute method works as expected."""
    class MockPlugin:
        """A mock plugin class for testing."""
        def execute(self):
            """Mock execute method."""
            return "Executed"

    plugin = MockPlugin()
    empty_plugin_manager.register_plugin("test_plugin", plugin)
    registered_plugin = empty_plugin_manager.get_plugin("test_plugin")
    assert registered_plugin.execute() == "Executed"  # Verifies execute method behavior
