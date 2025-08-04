from app import greet

def test_greet_with_name():
    assert greet(name="Samim") == "Hello, Samim!"

def test_greet_with_password():
    assert greet(password="12345") == "Hello, your password is 12345"

def test_greet_default():
    assert greet() == "Hello, World!"
