import os
import importlib
from src.plugins.plugin_interface import PluginInterface  # Add this import

class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin):
        """Register a new plugin."""
        if plugin is None:
            raise TypeError("Cannot register a None plugin.")  # Ensure we raise TypeError for None
        self.plugins[name] = plugin

    def get_plugin(self, name):
        """Retrieve a registered plugin."""
        return self.plugins.get(name, None)

    def list_plugins(self):
        """List all available plugins."""
        return self.plugins.keys()

    def load_plugins(self, plugin_directory):
        """Load plugins from the specified directory."""
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
                        plugin_instance = cls()  # Instantiate the plugin
                        self.register_plugin(module_name.lower(), plugin_instance)  # Use the module name as the key
