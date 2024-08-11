from typing import List

# Link to a tutorial about Python data structures
# Tutorial-1: https://youtu.be/daefaLgNkw0
# Official Python documentation on dictionaries
# Docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

"""
Dictionaries in Python are a versatile and powerful data type. They are collections of key-value pairs, where each key is unique. 
Unlike sequences such as lists, which are indexed by a range of numbers, dictionaries are indexed by keys. 
Keys can be any immutable type, such as strings or numbers. Tuples can also be used as dictionary keys as long as they only contain immutable elements.
However, lists and other mutable types cannot be used as dictionary keys because they can change over time, which would affect their use as a key.
"""

# Creating a dictionary with various types of data
student: dict = {
    'name': 'Jhon',  # Key 'name' with value 'Jhon'
    'age': 25,  # Key 'age' with value 25
    'courses': ['Math', 'Computer Science'],  # Key 'courses' with a list of course names
    'religion': 'Islam',  # Key 'religion' with value 'Islam'
    'section': 'A'  # Key 'section' with value 'A'
}

# Accessing the value associated with the key 'name'
print(student['name'])  # Output: Jhon
# Time Complexity: O(1) - Dictionary access by key is average-case constant time.
# Space Complexity: O(1) - No additional space used.

# Updating the value associated with the key 'name'
student['name'] = "Tom"
print(student.get('name'))  # Output: Tom
# Time Complexity: O(1) - Dictionary update by key is average-case constant time.
# Space Complexity: O(1) - No additional space used.

# Using the get() method to access the value for the key 'phone'
# If 'phone' is not found, it returns the default value "Default Student Phone"
print(student.get('phone', "Default Student Phone"))  # Output: Default Student Phone
# Time Complexity: O(1) - Dictionary get operation is average-case constant time.
# Space Complexity: O(1) - No additional space used.

# Updating multiple values in the dictionary at once
student.update({
    'name': 'Hulk',  # Updating the value of key 'name'
    'age': 20,  # Updating the value of key 'age'
    'phone': '234-76546-978'  # Adding a new key 'phone' with a value
})
# Time Complexity: O(k) - Where k is the number of key-value pairs updated.
# Space Complexity: O(1) - No additional space used, as the update operation modifies the dictionary in place.

# Printing the updated dictionary
print(student)  # Output: {'name': 'Hulk', 'age': 20, 'courses': ['Math', 'Computer Science'], 'phone': '234-76546-978'}
# Time Complexity: O(n) - Where n is the number of key-value pairs in the dictionary.
# Space Complexity: O(n) - Space required to hold the dictionary contents.

# Deleting the key 'religion' from the dictionary
del student['religion']
# Time Complexity: O(1) - Dictionary delete operation by key is average-case constant time.
# Space Complexity: O(1) - No additional space used.

# Removing and returning the value for the key 'section'
print(student.pop('section'))  # Output: A
# Time Complexity: O(1) - Dictionary pop operation by key is average-case constant time.
# Space Complexity: O(1) - No additional space used.

# Printing the dictionary after removing 'religion' and 'section'
print(student)  # Output: {'name': 'Hulk', 'age': 20, 'courses': ['Math', 'Computer Science'], 'phone': '234-76546-978'}
# Time Complexity: O(n) - Where n is the number of key-value pairs in the dictionary.
# Space Complexity: O(n) - Space required to hold the dictionary contents.

# Printing the number of key-value pairs in the dictionary
print(len(student))  # Output: 4
# Time Complexity: O(1) - Length retrieval is average-case constant time.
# Space Complexity: O(1) - No additional space used.

# Printing all the keys in the dictionary
print("Keys: ", student.keys())  # Output: Keys: dict_keys(['name', 'age', 'courses', 'phone'])
# Time Complexity: O(n) - Where n is the number of key-value pairs in the dictionary.
# Space Complexity: O(n) - Space required to iterate over the keys.

# Printing all the values in the dictionary
print("Values: ", student.values())  # Output: Values: dict_values(['Hulk', 20, ['Math', 'Computer Science'], '234-76546-978'])
# Time Complexity: O(n) - Where n is the number of key-value pairs in the dictionary.
# Space Complexity: O(n) - Space required to iterate over the values.

# Printing all key-value pairs in the dictionary as tuples
print("Key:Value: ", student.items())  # Output: Key:Value: dict_items([('name', 'Hulk'), ('age', 20), ('courses', ['Math', 'Computer Science']), ('phone', '234-76546-978')])
# Time Complexity: O(n) - Where n is the number of key-value pairs in the dictionary.
# Space Complexity: O(n) - Space required to iterate over the key-value pairs.

# Iterating over key-value pairs and printing them
for key, value in student.items():
    print(key, value)
    # Output:
    # name Hulk
    # age 20
    # courses ['Math', 'Computer Science']
    # phone 234-76546-978
    # Time Complexity: O(n) - Where n is the number of key-value pairs in the dictionary.
    # Space Complexity: O(1) - Iteration does not require additional space proportional to the size of the dictionary.

# Make comments and explain everything in the comments. Add more explanation here in the form of comments in terms of data structure. Determine time and space complexity (in comments). And use static typing properly
