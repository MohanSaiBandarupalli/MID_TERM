# src/plugins/power_plugin.py

"""
This module defines the PowerPlugin class, which implements a power operation plugin.
"""

from src.plugins.plugin_interface import PluginInterface

class PowerPlugin(PluginInterface):
    """
    A plugin to perform exponentiation. It raises a base to the power of an exponent.
    """
    def execute(self, *args):  # Use *args to match the interface
        """
        Raises the base to the power of the exponent.

        Args:
            *args: A variable number of arguments. Must contain exactly two elements.

        Returns:
            float: The result of the power operation.

        Raises:
            ValueError: If the number of arguments is not exactly two.
        """
        if len(args) != 2:
            raise ValueError("PowerPlugin requires exactly two arguments: base and exponent.")
        base, exponent = args  # Unpack the arguments
        return base ** exponent
