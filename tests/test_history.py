"""
This module contains unit tests for the HistoryFacade class.
It verifies the functionality of saving and loading history records.
"""

import os
import pytest
from src.history_manager import HistoryFacade

# pylint: disable=redefined-outer-name

@pytest.fixture
def test_history_facade():
    """
    Fixture to initialize the HistoryFacade for testing.
    Cleans the history file before each test.
    """
    os.makedirs('./data', exist_ok=True)  # Create data directory if it doesn't exist

    history_facade = HistoryFacade()
    history_facade.history_file = "./data/test_calculation_history.csv"

    # Ensure the file is clean before testing
    if os.path.exists(history_facade.history_file):
        with open(history_facade.history_file, 'w', encoding='utf-8') as f:
            f.truncate()

    # Initialize the file with headers
    with open(history_facade.history_file, 'w', encoding='utf-8') as f:
        f.write("Operation,Data,Result\n")

    return history_facade

def test_save_and_load(test_history_facade):
    """
    Test saving and loading calculations using HistoryFacade.
    """
    test_history_facade.save_calculation("add", [5, 3], 8)

    # Check if the saved calculation exists
    data = test_history_facade.load_history()
    assert len(data) == 1
    assert data.iloc[0]["Operation"] == "add"
    assert data.iloc[0]["Result"] == 8

def test_simplified_methods(test_history_facade):
    """
    Test simplified methods of the HistoryFacade.
    """
    test_history_facade.save_calculation("multiply", [2, 4, 2], 16)
    data = test_history_facade.load_history()
    assert len(data) == 1
    assert data.iloc[0]["Operation"] == "multiply"
    assert data.iloc[0]["Result"] == 16

    # Clear the history
    test_history_facade.clear_history()
    assert os.path.exists(test_history_facade.history_file)
