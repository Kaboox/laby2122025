import os

name = os.getenv("USERNAME", "Unknown user")
print(f"Hello, {name}! This is a script using environment variables.")
