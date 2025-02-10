# Create:

# Create an empty set
my_set = set()

# Create a set with values
my_set = {1, 2, 3, 4, 5}

# Create a set dynamically
my_set = set(range(1, 6))  # {1, 2, 3, 4, 5}

# Create a set from a list (removes duplicates)
my_set = set([1, 2, 2, 3, 4])  # {1, 2, 3, 4}

# Read:

my_set = {1, 2, 3, 4, 5}

# Check if an element exists in the set
print(3 in my_set)  # Output: True
print(6 in my_set)  # Output: False

# Loop through the set
for item in my_set:
    print(item)  # Output: 1 2 3 4 5 (order may vary)

# Get the length of the set
print(len(my_set))  # Output: 5

# Update:

# Add Elements:

my_set = {1, 2, 3}

# Add a single element
my_set.add(4)  # {1, 2, 3, 4}

# Add multiple elements
my_set.update([5, 6])  # {1, 2, 3, 4, 5, 6}

# Remove Elements:

my_set = {1, 2, 3, 4}

# Remove an element (KeyError if not found)
my_set.remove(3)  # {1, 2, 4}

# Remove an element safely (no error if not found)
my_set.discard(5)  # No error if 5 doesn't exist

# Remove and return a random element
removed_item = my_set.pop()  # Removes a random element
print(removed_item)  # Output: (varies)

# Delete

my_set = {1, 2, 3, 4, 5}

# Clear all elements from the set
my_set.clear()
print(my_set)  # Output: set()

# Delete the set
del my_set
# print(my_set)  # Raises NameError: name 'my_set' is not defined
