import os

file_path = "20-Files/test.txt"

if os.path.exists(file_path):
    print(f"Location '{file_path}' exists")
else:
    print("Location doesnt exist")