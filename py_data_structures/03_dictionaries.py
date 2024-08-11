from typing import List

"""
Tutorial-1: https://youtu.be/daefaLgNkw0
Docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

Another useful data type built into Python is the dictionary (see Mapping Types — dict). Dictionaries are sometimes found in other languages as 
“associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, 
which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; 
if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified 
in place using index assignments, slice assignments, or methods like append() and extend().
"""

student: dict = {'name': 'Jhon', 'age': 25, 'courses': ['Math', 'Computer Science'], 'religion': 'Islam', 'section': 'A'}
print(student['name'])
student['name'] = "Tom"
print(student.get('name'))
print(student.get('phone', "Default Student Phone"))

# Update multiple value in the dictionary
student.update({'name': 'Hulk', 'age': 20, 'phone': '234-76546-978'})
print(student)
del student['religion']
print(student.pop('section'))

print(student)
print(len(student))
print("Keys: ", student.keys())
print("Values: ", student.values())
print("Key:Value: ", student.items())

for key, value in student.items():
    print(key, value)