"""
This module defines command classes for basic arithmetic operations (add, subtract,
multiply, divide.) using the Command pattern. Each command class is responsible for
executing a specific operation on the calculator.
"""
class Command:
    """
    A base class for all command types. Subclasses must implement the `execute` method.
    """
    # pylint: disable=too-few-public-methods
    def execute(self, *args):
        """
        Executes the command with the provided arguments.

        Args:
            *args: A variable number of arguments for the command.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError("Command must implement 'execute'")


class AddCommand(Command):
    """
    Command for performing addition.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, calculator, history_facade):
        self.calculator = calculator
        self.history_facade = history_facade

    def execute(self, *args):
        result = self.calculator.add(*args)
        self.history_facade.save_calculation("add", list(args), result)
        return result


class SubtractCommand(Command):
    """
    Command for performing subtraction.
    """
    # pylint: disable=too-few-public-methods, arguments-differ
    def __init__(self, calculator, history_facade):
        self.calculator = calculator
        self.history_facade = history_facade

    def execute(self, x, y):
        result = self.calculator.subtract(x, y)
        self.history_facade.save_calculation("subtract", [x, y], result)
        return result


class MultiplyCommand(Command):
    """
    Command for performing multiplication.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, calculator, history_facade):
        self.calculator = calculator
        self.history_facade = history_facade

    def execute(self, *args):
        result = self.calculator.multiply(*args)
        self.history_facade.save_calculation("multiply", list(args), result)
        return result


class DivideCommand(Command):
    """
    Command for performing division.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, calculator, history_facade):
        self.calculator = calculator
        self.history_facade = history_facade

    def execute(self, *args):
        result = self.calculator.divide(*args)
        self.history_facade.save_calculation("divide", list(args), result)
        return result
    