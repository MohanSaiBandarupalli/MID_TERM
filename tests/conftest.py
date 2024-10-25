"""
Configuration file for pytest fixtures and setup functions for testing.
"""

import os
import pytest
from src.history_manager import HistoryFacade

def setup_history_facade():
    """
    Sets up the HistoryFacade by clearing the test history file
    and adding headers.
    """
    history_facade = HistoryFacade()
    history_facade.history_file = "./data/test_calculation_history.csv"

    if os.path.exists(history_facade.history_file):
        with open(history_facade.history_file, 'w', encoding='utf-8') as f:
            f.truncate()

    with open(history_facade.history_file, 'w', encoding='utf-8') as f:
        f.write("Operation,Data,Result\n")

    return history_facade

@pytest.fixture
def history_facade_fixture():
    """
    Fixture to initialize a clean HistoryFacade instance for each test.
    """
    return setup_history_facade()
