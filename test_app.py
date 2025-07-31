from unittest.mock import patch
from app import greet

@patch('builtins.input', return_value='12345')
def test_greet(mock_input):
    assert greet() == "Hello, your password is 12345"

