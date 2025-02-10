# 1. Count Elements

my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.count(2))  # Output: 3

# Find Index

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3))  # Output: 2

# Check Membership

my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)  # Output: True
print(6 in my_tuple)  # Output: False

# Convert Tuple to List and Vice Versa

# Convert tuple to list
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Convert list back to tuple
updated_tuple = tuple(my_list)
print(updated_tuple)  # Output: (1, 2, 3, 4)

# Tuple Unpacking

my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)  # Output: 1 2 3

# Nested Tuples

nested_tuple = (1, (2, 3), (4, (5, 6)))
print(nested_tuple[1][1])  # Output: 3
print(nested_tuple[2][1][1])  # Output: 6

