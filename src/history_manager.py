"""
This module provides the `HistoryFacade` class for managing calculation history.
It includes methods to save, load, and clear historical calculation data in a CSV file.
"""

import os
import pandas as pd
from src import config


class HistoryFacade:
    """
    A facade class for handling calculation history operations,
    such as saving, loading, and clearing history stored in a CSV file.
    """

    def __init__(self):
        """Initializes the HistoryFacade with the path to the history file."""
        self.history_file = config.HISTORY_FILE

    def save_calculation(self, operation, numbers, result):
        """
        Saves a calculation result to the history file.

        Args:
            operation (str): The name of the operation performed.
            numbers (list): The numbers involved in the calculation.
            result (float): The result of the calculation.
        """
        data = pd.DataFrame([{
            "Operation": operation,
            "Data": numbers,
            "Result": result
        }])
        # Ensure the file has headers if it's empty
        if os.path.getsize(self.history_file) == 0:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                f.write("Operation,Data,Result\n")

        data.to_csv(self.history_file, mode='a', header=False, index=False)

    def load_history(self):
        """
        Loads the calculation history from the history file.

        Returns:
            pd.DataFrame: A DataFrame containing the calculation history.
        """
        return pd.read_csv(self.history_file)

    def clear_history(self):
        """Clears the calculation history by emptying the history file."""
        with open(self.history_file, 'w', encoding='utf-8') as f:
            f.truncate()
