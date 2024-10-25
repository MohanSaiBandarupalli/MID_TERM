"""
This module implements the PluginManager class for managing plugins dynamically.

The PluginManager class is responsible for registering, retrieving, listing, and loading plugins
from a specified directory. Plugins are expected to follow a standard interface for compatibility.
"""

import os
import importlib.util
from src.plugins.plugin_interface import PluginInterface  # Import the interface here

class PluginManager:
    """
    Manages plugins by allowing registration, retrieval, listing, and dynamic loading of plugins.

    Attributes:
        plugins (dict): A dictionary to store plugins with their names as keys.
    """

    def __init__(self):
        """Initialize the PluginManager with an empty dictionary of plugins."""
        self.plugins = {}

    def register_plugin(self, name, plugin):
        """
        Register a new plugin.

        Args:
            name (str): The name of the plugin to register.
            plugin (PluginInterface): An instance of a plugin implementing the PluginInterface.

        Raises:
            TypeError: If attempting to register a None plugin.
        """
        if plugin is None:
            raise TypeError("Cannot register a None plugin.")
        self.plugins[name] = plugin

    def get_plugin(self, name):
        """
        Retrieve a registered plugin by name.

        Args:
            name (str): The name of the plugin to retrieve.

        Returns:
            PluginInterface or None: The registered plugin instance if found, or None if not.
        """
        return self.plugins.get(name, None)

    def list_plugins(self):
        """
        List all available plugins.

        Returns:
            dict_keys: The keys of the plugins dictionary, representing plugin names.
        """
        return self.plugins.keys()

    def load_plugins(self, plugin_directory):
        """
        Load plugins from the specified directory.

        Args:
            plugin_directory (str): The directory from which to load plugins.

        This method dynamically loads each Python file in the directory (excluding __init__.py files)
        as a plugin. Each loaded plugin must implement the PluginInterface to be registered.
        """
        for filename in os.listdir(plugin_directory):
            if filename.endswith('.py') and not filename.startswith('__'):
                module_name = filename[:-3]  # Remove the '.py' extension
                file_path = os.path.join(plugin_directory, filename)

                # Use importlib.util to load the module directly
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for attr in dir(module):
                    cls = getattr(module, attr)
                    if isinstance(cls, type) and issubclass(cls, PluginInterface):
                        self.register_plugin(module_name, cls())  # Register using the module name
