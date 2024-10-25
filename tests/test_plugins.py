"""
This module contains unit tests for the PluginManager class and plugin interfaces.
It verifies the functionality of registering and retrieving plugins.
"""

import pytest
from src.plugin_manager import PluginManager
from src.plugins.plugin_interface import PluginInterface

# pylint: disable=redefined-outer-name

class TestPlugin(PluginInterface):
    """
    A test implementation of the PluginInterface for testing purposes.
    """
    def execute(self, *args):
        return "Plugin executed successfully"


class PowerPlugin(PluginInterface):
    """
    A plugin to perform exponentiation. It raises a base to the power of an exponent.
    """
    def execute(self, *args):  # Accepts a variable number of arguments
        if len(args) != 2:
            raise ValueError(
                "PowerPlugin requires exactly two arguments: base and exponent."
            )
        base, exponent = args  # Unpack the arguments
        return base ** exponent


@pytest.fixture
def unique_plugin_manager():  # Renamed fixture to avoid redefinition
    """
    Fixture to initialize the PluginManager for testing.
    """
    return PluginManager()


def test_register_and_retrieve_plugin(unique_plugin_manager):
    """
    Test the registration and retrieval of a plugin.
    """
    plugin = TestPlugin()
    unique_plugin_manager.register_plugin("test_plugin", plugin)

    retrieved_plugin = unique_plugin_manager.get_plugin("test_plugin")
    assert retrieved_plugin is not None
    assert isinstance(retrieved_plugin, PluginInterface)
    assert retrieved_plugin.execute() == "Plugin executed successfully"


def test_power_plugin(unique_plugin_manager):
    """
    Test the functionality of the PowerPlugin.
    """
    plugin = PowerPlugin()
    unique_plugin_manager.register_plugin("power", plugin)

    power_plugin = unique_plugin_manager.get_plugin("power")
    result = power_plugin.execute(2, 3)  # Call with two arguments
    assert power_plugin is not None
    assert isinstance(power_plugin, PluginInterface)
    assert result == 8


def test_power_plugin_invalid_arguments(unique_plugin_manager):
    """
    Test that PowerPlugin raises a ValueError if given an incorrect number of arguments.
    """
    plugin = PowerPlugin()
    unique_plugin_manager.register_plugin("power", plugin)

    power_plugin = unique_plugin_manager.get_plugin("power")

    # Attempt to call execute with incorrect number of arguments and assert it raises ValueError
    with pytest.raises(
        ValueError, match="PowerPlugin requires exactly two arguments: base and exponent."
    ):
        power_plugin.execute(2)  # Only one argument instead of two
