name = "Alice"
message = f"Hello, {name}! Welcome to the program."
msg = "Hello, " + name
bio = """I am Alice and I am learning Python.
I can do anything I want because it's a multiline string"""
vars = [name, message, msg, bio]
ops = [
    name.upper(),
    name.lower(),
    name.replace("Alice", "Bob"),
    name.startswith("A"),
    name[1:4],
    len(name),
]
for i in vars:
    print(i)
    if i == name:
        for i in ops:
            print(i)


# print(name.upper())
# print(name.lower())
# print(name.replace("Alice","Bob"))
# print(name.startswith("A"))
# print(name[1:4])
# print(len(name))
