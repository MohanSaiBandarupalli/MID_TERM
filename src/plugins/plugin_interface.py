"""
This module defines the PluginInterface class, which serves as a base interface
for all plugins. Plugins must implement the `execute` method.
"""

class PluginInterface:
    """
    A base interface for plugins. All plugins should inherit from this class
    and implement the `execute` method.
    """
    # pylint: disable=too-few-public-methods

    def execute(self, *args):
        """
        Executes the plugin's main functionality.

        Args:
            *args: A variable number of arguments for the plugin's execute method.

        Raises:
            NotImplementedError: If the plugin does not implement this method.
        """
        raise NotImplementedError("Plugins must implement 'execute'")
    