"""
This module defines the PluginInterface, which serves as a base interface for all plugins.

Each plugin is expected to inherit from PluginInterface and implement the `execute` method
to define its main functionality. This ensures that plugins adhere to a consistent structure.
"""

# src/plugins/plugin_interface.py

class PluginInterface:
    """
    A base interface for plugins. All plugins should inherit from this class
    and implement the `execute` method.
    """

    def execute(self, *args):
        """
        Executes the plugin's main functionality.

        Args:
            *args: A variable number of arguments for the plugin's execute method.

        Raises:
            NotImplementedError: If the plugin does not implement this method.
        """
        raise NotImplementedError("Plugins must implement 'execute'")
