# Create:
# Create an empty dictionary
my_dict = {}

# Create a dictionary with initial key-value pairs
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Create a dictionary dynamically
keys = ["name", "age", "city"]
values = ["Bob", 30, "London"]
my_dict = dict(zip(keys, values))  # Output: {'name': 'Bob', 'age': 30, 'city': 'London'}

# Read

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Access value by key
print(my_dict["name"])  # Output: Alice

# Use get() to avoid KeyError if the key doesn't exist
print(my_dict.get("age"))  # Output: 25
print(my_dict.get("country", "Not Found"))  # Output: Not Found

# Check if a key exists
print("city" in my_dict)  # Output: True
print("country" in my_dict)  # Output: False

# Iterate through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for value in my_dict.values():
    print(value)
# Output:
# Alice
# 25
# New York

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
if 25 in my_dict.values():
    print("25 exists in the dictionary.")  # Output: 25 exists in the dictionary.

# Update

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Update an existing value
my_dict["age"] = 26

# Add a new key-value pair
my_dict["country"] = "USA"

# Merge another dictionary
my_dict.update({"profession": "Engineer", "age": 27})

print(my_dict)
# Output: {'name': 'Alice', 'age': 27, 'city': 'New York', 'country': 'USA', 'profession': 'Engineer'}

# Delete

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Remove a specific key-value pair using pop()
my_dict.pop("age")  # Output: 25

# Remove and get the last inserted key-value pair (Python 3.7+)
last_item = my_dict.popitem()
print(last_item)  # Output: ('city', 'New York')

# Clear the entire dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# Delete the dictionary
del my_dict
# print(my_dict)  # Raises NameError: name 'my_dict' is not defined


# Get Keys, Values, and Items

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Get all keys
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

# Get all values
print(my_dict.values())  # Output: dict_values(['Alice', 25, 'New York'])

# Get all key-value pairs
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])


# Loop:

# How can you loop through a dictionary?

# Loop through keys: for key in my_dict:.
# Loop through values: for value in my_dict.values():.
# Loop through key-value pairs: for key, value in my_dict.items():