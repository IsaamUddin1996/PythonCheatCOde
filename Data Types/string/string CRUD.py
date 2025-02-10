#  String Properties
# Immutable: Strings cannot be modified in place. Any update creates a new string object.
# Iterable: You can loop through a string character by character.

s = ", ".join(['hello', 'world'])  # 'hello world'
print(s)

# substrings
data = "Hello World"
print(data[0:3])

# find(substring)
"Hello".find("l")  # Output: 2

# index(substring)
"Hello".index("l")  # Output: 2
# count(substring)
"Hello Hello".count("Hello")  # Output: 2

"hello world".title()  # Output: 'Hello World'
# swapcase()
"Hello".swapcase()  # Output: 'hELLO'

#Replace(Old,New)

rp = data.replace("Hello","Hi")
print(rp)

#Delete

v_delete = "Hi"
del v_delete
print(v_delete)

result = "Hello" + " " + "World"
result = "Ha" * 3  # Outputs: HaHaHa

# Membership
print("World" in "Hello, World!")  # Outputs: True

# transform
text = "python"
print(text.upper())  # Outputs: PYTHON
print(text.capitalize())  # Outputs: Python

# Split and Join:

data = "one, two, three"
words = data.split(", ")  # Splits into ['one', 'two', 'three']
print(words)
"hello world".split()  # ['hello', 'world']
" ".join(['hello', 'world'])  # 'hello world'

joined = ", ".join(words)  # Joins into 'one, two, three'
print(joined)
# Advanced Use: Using a limit on splits:
text = "name:John Doe:age:30"
parts = text.split(":", maxsplit=2)  # Outputs: ['name', 'John Doe', 'age:30']

# strip
"  Hello  ".strip()  # Output: 'Hello'

# lstrip
"  Hello".lstrip()  # Output: 'Hello'

# rstrip
"Hello  ".rstrip()  # Output: 'Hello'

#startswith

filename = "report_2025.pdf"
if filename.startswith("report"):
    print("This is a report file.")  # Outputs: This is a report file.

# endswith
file = "image.jpg"
if file.endswith(".jpg") or file.endswith(".png"):
    print("This is an image file.")  # Outputs: This is an image file.

