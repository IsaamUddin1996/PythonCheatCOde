# Additional Set Operations

# 1. Union of Sets

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}

# 2.Intersection of Sets

print(set1.intersection(set2))  # Output: {3}

# 3. Difference of Sets

print(set1.difference(set2))  # Output: {1, 2}

# 4. Symmetric Difference

print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}

# 5. Subset and Superset

set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # Output: True
print(set2.issuperset(set1))  # Output: True

# 6. Convert Set to List

my_set = {1, 2, 3}
my_list = list(my_set)
print(my_list)  # Output: [1, 2, 3] (order may vary)
