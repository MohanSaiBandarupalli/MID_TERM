"""
This module contains unit tests for the PluginManager class and plugin interfaces.
It verifies the functionality of registering and retrieving plugins.
"""
# pylint: disable=redefined-outer-name
import pytest
from src.plugin_manager import PluginManager
from src.plugins.plugin_interface import PluginInterface

class TestPlugin(PluginInterface):
    """A test implementation of the PluginInterface for testing purposes."""
    def execute(self, *args):
        return "Plugin executed successfully"

class PowerPlugin(PluginInterface):
    """A plugin to perform exponentiation."""
    def execute(self, *args):
        """Raises the base to the power of the exponent."""
        if len(args) != 2:
            raise ValueError("PowerPlugin requires exactly two arguments: base and exponent.")
        base, exponent = args
        return base ** exponent

@pytest.fixture
def unique_plugin_manager():
    """Fixture to initialize the PluginManager for testing."""
    return PluginManager()

def test_register_and_retrieve_plugin(unique_plugin_manager):
    """Test the registration and retrieval of a plugin."""
    plugin = TestPlugin()
    unique_plugin_manager.register_plugin("test_plugin", plugin)

    retrieved_plugin = unique_plugin_manager.get_plugin("test_plugin")
    assert retrieved_plugin is not None
    assert isinstance(retrieved_plugin, PluginInterface)
    assert retrieved_plugin.execute() == "Plugin executed successfully"

def test_power_plugin(unique_plugin_manager):
    """Test the functionality of the PowerPlugin."""
    plugin = PowerPlugin()
    unique_plugin_manager.register_plugin("power", plugin)

    power_plugin = unique_plugin_manager.get_plugin("power")
    result = power_plugin.execute(2, 3)  # Call with two arguments
    assert power_plugin is not None
    assert isinstance(power_plugin, PluginInterface)
    assert result == 8

def test_dynamic_plugin_loading(unique_plugin_manager, tmp_path):
    """Test dynamic loading of plugins from a directory."""
    # Create a temporary plugin file
    plugin_code = """
from src.plugins.plugin_interface import PluginInterface

class TempPlugin(PluginInterface):
    def execute(self):
        return "Temp Plugin executed"
"""
    plugin_file = tmp_path / "temp_plugin.py"
    plugin_file.write_text(plugin_code)

    # Load plugins from the temporary directory
    unique_plugin_manager.load_plugins(str(tmp_path))

    # Check if the plugin was registered correctly
    assert "temp_plugin" in unique_plugin_manager.list_plugins()  # Match the registered name

def test_register_none_plugin(unique_plugin_manager):
    """Test registering a None as a plugin."""
    with pytest.raises(TypeError):
        unique_plugin_manager.register_plugin("none_plugin", None)
