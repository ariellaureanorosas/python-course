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
from encodings import utf_8

base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "lesson120_teste.txt")

with open(path, "w+", encoding=utf_8) as file:
    file.write("Hello Word\n")
    file.write("line 2\n")
    file.writelines(("line 3\n", "line 4\n", "line 5\n"))
    file.seek(0, 0)
    print(file.read())
    file.seek(0, 0)
    print("-" * 10)
    print("lendo")
    print(file.readline(), end="")
    print(file.readline().strip())
    print("-" * 10)
    print("READLINES")
    for line in file.readlines():
        print(line.strip())
    print("-" * 10)
