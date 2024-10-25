"""
Main module for the calculator application.
Runs a REPL (Read-Eval-Print Loop) for command and plugin execution.
"""

from src.calculator import Calculator
from src.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from src.history_manager import HistoryFacade
from src.plugin_manager import PluginManager
from src.plugins.power_plugin import PowerPlugin  # Example plugin for power calculations
from src.logger import logger  # Import your logger

def run():
    """Entry point for the calculator application."""
    logger.info("Starting the calculator application.")
    calculator = Calculator()
    history_facade = HistoryFacade()
    plugin_manager = PluginManager()

    # Register the PowerPlugin directly
    plugin_manager.register_plugin("power", PowerPlugin())

    command_dict = initialize_commands(calculator, history_facade, plugin_manager)

    # Show commands immediately on startup, including the menu option
    show_commands(command_dict)

    while True:
        command_input = input(">> ").strip().lower()
        logger.debug(f"User input: {command_input}")  # Log user input
        if is_exit_command(command_input):
            logger.info("Exiting the calculator application.")
            break

        command_name, args = parse_command(command_input, command_dict)
        if not command_name:
            logger.warning("Unknown command entered.")
            print("Unknown command. Type 'menu' to see available commands.")
            continue

        handle_command(command_name, args, command_dict, history_facade)

def initialize_commands(calculator, history_facade, plugin_manager):
    """Initializes the core calculator commands and plugin commands."""
    command_dict = {
        "add": AddCommand(calculator, history_facade),
        "subtract": SubtractCommand(calculator, history_facade),
        "multiply": MultiplyCommand(calculator, history_facade),
        "divide": DivideCommand(calculator, history_facade),
        "load_history": 'load_history',
        "clear_history": 'clear_history',
        "menu": "menu"  # Add the menu command to the dictionary
    }

    # Add all loaded plugins to the command dictionary
    for plugin_name in plugin_manager.list_plugins():
        command_dict[plugin_name] = plugin_manager.get_plugin(plugin_name)

    return command_dict

def show_commands(command_dict):
    """Displays available commands to the user."""
    print("Available commands:")
    for command in command_dict:
        if command in ['load_history', 'clear_history', 'menu']:
            print(f">> {command} --> {command}")  # Display special commands
        else:
            print(f">> {command} --> {command} num1 num2 (or other required arguments)")

def is_exit_command(command_input):
    """Checks if the user entered an exit command."""
    return command_input in ["exit", "q", "quit", "Q"]

def parse_command(command_input, command_dict):
    """Parses user input to identify the command and arguments."""
    parts = command_input.split()
    command_name = parts[0] if parts else None
    args = parse_arguments(parts[1:]) if len(parts) > 1 else []
    return command_name if command_name in command_dict else None, args

def parse_arguments(arg_strings):
    """Converts the argument strings to float values."""
    try:
        return list(map(float, arg_strings))
    except ValueError:
        print("Invalid arguments. Please provide numbers.")
        return []

def handle_command(command_name, args, command_dict, history_facade):
    """Handles command execution based on user input."""
    try:
        logger.info(f"Executing command: {command_name} with arguments: {args}")
        if command_name == "load_history":
            handle_load_history(history_facade)
        elif command_name == "clear_history":
            handle_clear_history(history_facade)
        elif command_name == "menu":
            show_commands(command_dict)  # Show commands if the user types "menu"
        else:
            execute_command(command_name, args, command_dict)
    except ValueError as e:
        logger.error(f"Value error occurred: {e}")
        print(f"Value error occurred: {e}")
    except KeyError as e:
        logger.error(f"Key error occurred: {e}")
        print(f"Key error occurred: {e}")
    except TypeError as e:
        logger.error(f"Type error occurred: {e}")
        print(f"Type error occurred: {e}")

def handle_load_history(history_facade):
    """Loads and displays the calculation history."""
    try:
        load_history = history_facade.load_history()
        print(load_history)
    except FileNotFoundError:
        print("No data found.")

def handle_clear_history(history_facade):
    """Clears the calculation history."""
    history_facade.clear_history()
    print("History cleared successfully.")

def execute_command(command_name, args, command_dict):
    """Executes the specified command."""
    command = command_dict[command_name]
    if isinstance(command, (AddCommand, SubtractCommand, MultiplyCommand, DivideCommand)):
        result = command.execute(*args)
        print(f"Result: {result}")
    else:
        result = command.execute(*args)  # Call PowerPlugin's execute method
        print(f"Plugin Result: {result}")

if __name__ == "__main__":
    run()
