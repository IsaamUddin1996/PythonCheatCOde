# Some interview Questions for string

# Frequency Calculation

sentence = "Hello, World!"

# Initialize an empty dictionary to store frequency
frequency = {}

# Iterate through each character in the sentence
for char in sentence:
    if char in frequency:
        frequency[char] += 1  # Increment count if character exists in dictionary
    else:
        frequency[char] = 1  # Add character to dictionary with count 1

# Print the frequency dictionary
print(frequency)

# Reverse and loop through a string
s = "hello"
for char in reversed(s):
    print(char, end="")  # Output: "olleh"

palindrome_string = "madam"
new_pal = palindrome_string.split()[::-1]
new_pal = "".join(new_pal)
print(new_pal)
if new_pal == palindrome_string:
    print("It is palindrome") 
else:
    print("It is not a palindrome")

# Count Vowels and consonants

def count_vowels_consonants(s):
    vowels = "aeiou"
    s = s.lower()
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Example
v = count_vowels_consonants("Hello Worl")
print(v)
vowels, consonants = count_vowels_consonants("Hello World")
print(f"Vowels: {vowels}, Consonants: {consonants}")  # Output: Vowels: 3, Consonants: 7

# Remove Duplicates
def remove_duplicates(s):
    seen = set()
    result = ""

    for char in s:
        if char not in seen:
            seen.add(char)
            result += char

    return result

# Example
print(remove_duplicates("aabbcc"))  # Output: "abc"

# Duplicate 

def find_duplicates(s):
    seen = set()  # To track characters we've seen
    duplicates = set()  # To track duplicates

    for char in s:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)

    return list(duplicates)  # Convert the duplicates set to a list for the output

# Example
print(find_duplicates("aabbccdde"))  # Output: ['a', 'b', 'c', 'd']

# count words 

def count_words(s):
    words = s.split()  # Split the string by whitespace into a list of words
    return len(words)  # Return the number of words

# Example
print(count_words("Hello, World! How are you?"))  # Output: 5
