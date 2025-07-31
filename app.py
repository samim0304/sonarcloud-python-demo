def greet(name):
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"


password = input("Enter password: ")
print("Password is:", password)

print(greet("Samim"))
