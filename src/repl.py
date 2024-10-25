"""
This module provides a REPL interface for interacting with the calculator.
"""

from src.plugin_manager import PluginManager

def run_repl():
    """Runs the REPL loop for user interaction with the calculator."""
    plugin_manager = PluginManager()
    plugin_manager.load_plugins('src/plugins')  # Ensure this directory is correct

    while True:
        command = input("Enter command (or 'menu' for available commands): ")

        if command == 'menu':
            plugins = plugin_manager.list_plugins()
            print("Available Plugins:")
            for name in plugins:
                print(f"{name}")
        elif command in plugin_manager.plugins:
            args = input("Enter arguments: ").split()
            try:
                result = plugin_manager.get_plugin(command).execute(*map(float, args))
                print("Result:", result)
            except Exception as e:
                print("Error:", str(e))
        elif command == 'exit':
            break
        else:
            print("Unknown command. Type 'menu' to see available commands.")

if __name__ == "__main__":
    run_repl()
