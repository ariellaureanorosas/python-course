# Creating files with Python + Context Manager with
# We use the function 'open' for open
# a file in Python (It may or may not exist)
# Modes:
# r (reading), w (written), x (for breeding)
# a (write at the end), b (binary)
# t (text mode), + (reading and writing)
# Context manager - with (open and close)
# Useful Methods:
# write, read
# writelines
# seek
# readline
# readlines
# Let's talk more about the OS module, but:
# os.remove or unlink - apaga o arquivo
# os.rename - renme or move the file
# let's talk about more the JSON module, about:
# json.dump = Generate one file json
# json.load

# path = "lesson119_teste.txt"

# with open(path, "w") as file:
#     print("Hello Word")
#     print("The file will be closed")

import os

base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "lesson119_teste.txt")

with open(path, "w") as file:
    file.write("Hello Word\n")
    print("File created")
    print("The file will be closed")
