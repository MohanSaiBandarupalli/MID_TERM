"""
This module contains the Calculator class which implements basic arithmetic operations.
"""

class Calculator:
    """
    A class used to perform basic arithmetic operations such as addition, subtraction,
    multiplication, and division.
    """

    def add(self, *args):
        """
        Performs the addition of multiple numbers.

        Args:
            *args: A variable number of numeric arguments to add together.

        Returns:
            float: The sum of all the arguments.
        """
        return sum(args)

    def subtract(self, x, y):
        """
        Performs subtraction of two numbers.

        Args:
            x (float): The number from which to subtract.
            y (float): The number to subtract from x.

        Returns:
            float: The result of subtracting y from x.
        """
        return x - y

    def multiply(self, *args):
        """
        Performs multiplication of multiple numbers.

        Args:
            *args: A variable number of numeric arguments to multiply together.

        Returns:
            float: The product of all the arguments.

        Raises:
            ValueError: If no arguments are provided.
        """
        if len(args) == 0:
            raise ValueError("At least one number is required for multiplication.")
        result = 1
        for number in args:
            result *= number
        return result

    def divide(self, *args):
        """
        Performs division of multiple numbers.

        Args:
            *args: A variable number of numeric arguments to divide.

        Returns:
            float: The result of dividing the first argument by the subsequent arguments.

        Raises:
            ValueError: If fewer than two arguments are provided or if division by zero is attempted.
        """
        if len(args) < 2:
            raise ValueError("At least two numbers are required for division.")
        if 0 in args[1:]:
            raise ValueError("Division by zero is not allowed.")
        
        result = args[0]
        for number in args[1:]:
            result /= number
        return result
