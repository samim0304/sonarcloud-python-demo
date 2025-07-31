from app import greet

def test_greet_name():
    assert greet("Samim") == "Hello, Samim!"

def test_greet_default():
    assert greet("") == "Hello, World!"
