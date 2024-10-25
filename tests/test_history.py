"""
This module contains unit tests for the HistoryFacade class.
It verifies the functionality of saving and loading history records.
"""

import os
import pytest

# Import the HistoryFacade fixture from conftest
@pytest.fixture(autouse=True)
def use_history_facade_fixture(history_facade_fixture):
    """Use the shared history_facade_fixture for all tests in this module."""
    return history_facade_fixture

def test_save_and_load(history_facade_fixture):
    """
    Test saving and loading calculations using HistoryFacade.
    """
    history_facade_fixture.save_calculation("add", [5, 3], 8)

    # Check if the saved calculation exists
    data = history_facade_fixture.load_history()
    assert len(data) == 1
    assert data.iloc[0]["Operation"] == "add"
    assert data.iloc[0]["Result"] == 8


def test_simplified_methods(history_facade_fixture):
    """
    Test simplified methods of the HistoryFacade.
    """
    history_facade_fixture.save_calculation("multiply", [2, 4, 2], 16)
    data = history_facade_fixture.load_history()
    assert len(data) == 1
    assert data.iloc[0]["Operation"] == "multiply"
    assert data.iloc[0]["Result"] == 16

    # Clear the history
    history_facade_fixture.clear_history()
    assert os.path.exists(history_facade_fixture.history_file)
    assert len(history_facade_fixture.load_history()) == 0
