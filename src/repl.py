from src.plugin_manager import PluginManager

def run_repl():
    plugin_manager = PluginManager()
    plugin_manager.load_plugins('src/plugins')  # Ensure this directory is correct

    while True:
        command = input("Enter command (or 'menu' for available commands): ")

        if command == 'menu':
            plugins = plugin_manager.list_plugins()
            print("Available Plugins:")
            for name, info in plugins.items():
                print(f"{name}: {info}")
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
