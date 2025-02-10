my_list = [1, 2, 3, 4, 5]
my_list = [x for x in range(1, 6)]  # [1, 2, 3, 4, 5]

# Read
print(my_list[1:4])  # Output: [2, 3, 4]

# Loop through the list
for item in my_list:
    print(item) 

# Update

my_list[2] = 99 
# Add an element to the end
my_list.append(6)

# Insert an element at a specific index
my_list.insert(2, 50)  # Insert 50 at index 2
print(my_list)  # Output: [1, 2, 50, 99, 4, 5, 6]

# Extend the list with another list
my_list.extend([7, 8])
print(my_list)  # Output: [1, 2, 50, 99, 4, 5, 6, 7, 8]

# Delete

my_list = [1, 2, 3, 4, 5]

# Remove an element by value
my_list.remove(3)  # Remove the first occurrence of 3
print(my_list)  # Output: [1, 2, 4, 5]

# Remove an element by index
del my_list[1]  # Removes the element at index 1
print(my_list)  # Output: [1, 4, 5]

# Remove the last element
my_list.pop()
print(my_list)  # Output: [1, 4]

# Clear the entire list
my_list.clear()
print(my_list)  # Output: []

