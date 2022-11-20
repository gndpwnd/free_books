# Path: books.txt

filename = "books.txt"

names = []

with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        names.append(line)

with open(filename, "w") as f:
    for name in names:
        name = name.replace("\n", "")
        f.write("\"" + name + "\",\n")
