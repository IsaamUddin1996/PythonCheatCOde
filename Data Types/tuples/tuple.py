# Create:

# Create an empty tuple
my_tuple = ()

# Create a tuple with values
my_tuple = (1, 2, 3)

# Create a tuple without parentheses (implicit)
my_tuple = 1, 2, 3

# Create a single-element tuple (note the trailing comma)
my_tuple = (1,)  # Without the comma, it would be an integer

# Create a tuple dynamically from an iterable
my_tuple = tuple(range(1, 6))  # (1, 2, 3, 4, 5)

# Read

my_tuple = (1, 2, 3, 4, 5)

# Access by index
print(my_tuple[0])  # Output: 1

# Access the last element
print(my_tuple[-1])  # Output: 5

# Slice the tuple
print(my_tuple[1:4])  # Output: (2, 3, 4)

# Loop through the tuple
for item in my_tuple:
    print(item)  # Output: 1 2 3 4 5

# Update

# Tuples are immutable, so their elements cannot be changed. However, you can:

# Reassign the entire tuple.
# Create a new tuple by combining or modifying existing tuples.

my_tuple = (1, 2, 3)

# Reassign a new tuple
my_tuple = (1, 2, 3, 4)  # New tuple

# Concatenate tuples to create a new one
new_tuple = my_tuple + (5, 6)
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Multiply tuples
multiplied_tuple = my_tuple * 2
print(multiplied_tuple)  # Output: (1, 2, 3, 1, 2, 3)

# Delete

my_tuple = (1, 2, 3, 4, 5)

# Delete the entire tuple
del my_tuple

print(my_tuple)  # Raises NameError: name 'my_tuple' is not defined

