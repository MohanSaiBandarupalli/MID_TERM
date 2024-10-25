"""
This module contains unit tests for the Calculator and its associated command classes.
It verifies the functionality of addition, subtraction, multiplication, and division commands.
"""

from src.calculator import Calculator
from src.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command(history_facade_fixture):
    """
    Test addition command functionality and history saving.
    """
    calculator = Calculator()
    add_command = AddCommand(calculator, history_facade_fixture)

    result = add_command.execute(10, 5)
    assert result == 15

    data = history_facade_fixture.load_history()
    assert len(data) == 1
    assert data.iloc[0]["Operation"] == "add"
    assert data.iloc[0]["Result"] == 15

def test_subtract_command(history_facade_fixture):
    """
    Test subtraction command functionality and history saving.
    """
    calculator = Calculator()
    subtract_command = SubtractCommand(calculator, history_facade_fixture)

    result = subtract_command.execute(10, 5)
    assert result == 5

    data = history_facade_fixture.load_history()
    assert len(data) == 1
    assert data.iloc[0]["Operation"] == "subtract"
    assert data.iloc[0]["Result"] == 5

def test_multiply_command(history_facade_fixture):
    """
    Test multiplication command functionality and history saving.
    """
    calculator = Calculator()
    multiply_command = MultiplyCommand(calculator, history_facade_fixture)

    result = multiply_command.execute(3, 7)
    assert result == 21

    data = history_facade_fixture.load_history()
    assert len(data) == 1
    assert data.iloc[0]["Operation"] == "multiply"
    assert data.iloc[0]["Result"] == 21

def test_divide_command(history_facade_fixture):
    """
    Test division command functionality and history saving.
    """
    calculator = Calculator()
    divide_command = DivideCommand(calculator, history_facade_fixture)

    result = divide_command.execute(15, 3)
    assert result == 5

    data = history_facade_fixture.load_history()
    assert len(data) == 1
    assert data.iloc[0]["Operation"] == "divide"
    assert data.iloc[0]["Result"] == 5
