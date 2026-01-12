# Palindrome
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("madam"))   # True
print(is_palindrome("hello"))   # False

# Min & Max

def find_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]

    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val

print(find_min_max([5, 2, 9, 1, 7]))
# Output: (1, 9)

# Even or Odd
def is_even(n):
    return n % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False


# Reverse a String

# Python – Using a Loop (manual method)

def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

print(reverse_string("hello"))   # olleh

# Python – Two-Pointer Method (best logically)

def reverse_string(s):
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return "".join(s)

print(reverse_string("hello"))