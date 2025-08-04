import os

def greet(name=None, password=None):
    if name:
        return f"Hello, {name}!"
    if password:
        return f"Hello, your password is {password}"
    return "Hello, World!"

if __name__ == "__main__":
    password = os.getenv("APP_PASSWORD", "12345")
    print(greet(password=password))
