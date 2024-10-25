"""
This module contains the PowerPlugin class for exponentiation functionality.
"""

from src.plugins.plugin_interface import PluginInterface

class PowerPlugin(PluginInterface):
    """A plugin to perform exponentiation."""

    def execute(self, *args):
        """Raises the base to the power of the exponent."""
        if len(args) != 2:
            raise ValueError("PowerPlugin requires exactly two arguments: base and exponent.")
        base, exponent = args
        return base ** exponent
