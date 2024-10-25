"""
This module defines the PowerPlugin class, which implements a power operation plugin.
"""

from src.plugins.plugin_interface import PluginInterface

class PowerPlugin(PluginInterface):
    """
    A plugin to perform exponentiation. It raises a base to the power of an exponent.
    """
    def execute(self, *args):
        """
        Executes the power operation.

        Args:
            *args: A variable number of arguments where:
                args[0] (float): The base number.
                args[1] (float): The exponent to raise the base to.

        Returns:
            float: The result of raising the base to the exponent.

        Raises:
            ValueError: If the number of arguments is not exactly two.
        """
        if len(args) != 2:
            raise ValueError("PowerPlugin requires exactly two arguments: base and exponent.")
        
        base, exponent = args  # Unpack the arguments
        return base ** exponent
