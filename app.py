import os
def greet(name):
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"


password = os.getenv("APP_PASSWORD", "12345")
print("Password is:", password)

def greet(password=None):
    if password is None:
        # fallback for local dev (optional)
        password = "default123"
    return f"Hello, your password is {password}"


print(greet("Samim"))
