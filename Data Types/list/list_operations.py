# # Sorting Ascending Descending

# my_list = [3, 1, 4, 2, 5]
# my_list.sort()  # Sort the list in ascending order
# print(my_list)  # Output: [1, 2, 3, 4, 5]

# my_list.sort(reverse=True)  # Sort in descending order
# print(my_list)  # Output: [5, 4, 3, 2, 1]

# # Length
# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))  # Output: 5

# # Check for Existence:

# my_list = [1, 2, 3, 4, 5]
# print(3 in my_list)  # Output: True
# print(6 in my_list)  # Output: False

x = [1,2,3]
y = x
print(y)
x.append(2)
print(x)
print(y)

                                    # Interview Question Answers

def reverse_list(lst):
    reversed_list = []
    for item in lst:  # Loop through each element in the original list
        reversed_list.insert(0, item)  # Insert each element at the beginning of the new list
    return reversed_list

# Example Usage
print(reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]

original_list = [3,2,1]
reverse_list = original_list[::-1].copy()
print(reverse_list)

# Find min and max 

def find_min_max(lst):
    sorted_list = sorted(lst)  # Sort the list
    return sorted_list[0], sorted_list[-1]  # First and last elements are min and max

# Example Usage
print(find_min_max([3, 1, 4, 1, 5, 9]))  # Output: (1, 9)

def find_max_min(lst):
    max_val = lst[0]
    min_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val

print(find_max_min([3, 1, 4, 1, 5, 9]))  # Output: (9, 1)

# count occurances 

def count_occurrences(lst, target):
    count = 0
    for num in lst:
        if num == target:
            count += 1
    return count

print(count_occurrences([1, 2, 2, 3, 4, 2], 2))  # Output: 3

# Check Palindrome

def is_palindrome(lst):
    return lst == lst[::-1]

print(is_palindrome([1, 2, 3, 2, 1]))  # Output: True

# Merge Two Lists

def merge_lists(lst1, lst2):
    return lst1 + lst2

print(merge_lists([1, 2], [3, 4]))  # Output: [1, 2, 3, 4]

# Remove Duplicates 
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 3, 3, 4]))  # Output: [1, 2, 3, 4]

# Find Second Largest Value

def find_second_largest(lst):
    # Convert to set to remove duplicates, then sort the unique values
    unique_values = sorted(set(lst), reverse=True)
    
    # Check if there are at least two unique values
    if len(unique_values) < 2:
        return None  # No second largest value if less than 2 unique elements
    
    return unique_values[1]  # Return the second largest value

# Example Usage
print(find_second_largest([4, 2, 1, 3, 4, 5, 5]))  # Output: 4
print(find_second_largest([10, 10, 10]))           # Output: None

                                # Sort list without using sort 

# Bubble Sort

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:  # Compare adjacent elements
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap if needed
    return lst

# Example Usage
print(bubble_sort([4, 2, 7, 1, 9]))  # Output: [1, 2, 4, 7, 9]
