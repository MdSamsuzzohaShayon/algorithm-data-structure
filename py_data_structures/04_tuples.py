from typing import List, Tuple, Any, Dict
from timeit import timeit

# Link to a tutorial about Python data structures
# Tutorial-1: https://youtu.be/daefaLgNkw0
# Official Python documentation on tuples
# Docs: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

"""
Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples are immutable, and usually contain a 
heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). 
Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
"""

# List definition with mixed data types
alist: List[Any] = ["a", 'b', 12]  # mutable: Can be modified, items can be of any type
print(type(alist))  # Output: <class 'list'>

# Modifying the list
alist[0] = 'x'  # Changes the first element from 'a' to 'x'
print(alist)  # Output: ['x', 'b', 12]

# Tuple definition with mixed data types
atuple: Tuple[str, str, int] = ("c", 'd', 13)  # immutable: Cannot be modified once created
print(type(atuple))  # Output: <class 'tuple'>

# Single-element tuple (note the comma)
atuple2: Tuple[int] = (5,)  # Single-element tuple
print(type(atuple2))  # Output: <class 'tuple'>

# Uncommenting the next line will raise an error since tuples are immutable
# atuple[0] = 'f'  # TypeError: 'tuple' object does not support item assignment

# Speed test for lists
list_speed = timeit(stmt='["red", "blue", "green", 6, 7, 12, 18, "dude"]', number=10000000)
print(f"List creation time: {list_speed} seconds")
# Time Complexity: O(n) for creating a list of n elements.
# Space Complexity: O(n) for storing n elements in the list.

# Speed test for tuples
tuple_speed = timeit(stmt='("red", "blue", "green", 6, 7, 12, 18, "dude")', number=10000000)
print(f"Tuple creation time: {tuple_speed} seconds")
# Time Complexity: O(n) for creating a tuple of n elements.
# Space Complexity: O(n) for storing n elements in the tuple.

# Memory efficiency comparison
# Lists are stored in multiple memory blocks to accommodate dynamic resizing.
# Tuples are stored in a single memory block, which makes them more memory-efficient.

# Unpacking a tuple into variables
(fl, sl, nu) = atuple  # Unpacks the tuple into three variables
print(fl, sl, nu)  # Output: c d 13
# Time Complexity: O(1) - Tuple unpacking is constant time as it involves fixed number of elements.
# Space Complexity: O(1) - No additional space required.

print("=================== Use cases ================")

"""
Tuples in Python are immutable sequences, which means once they are created, they cannot be changed. This immutability gives tuples certain advantages and use cases compared to other data structures 
like lists. Here are some situations where using tuples is particularly beneficial:
"""

# 1. Immutable Data Storage
point: Tuple[int, int] = (10, 20)  # Coordinates are fixed and should not change
# Time Complexity: O(1) - Accessing elements is constant time.
# Space Complexity: O(1) - Tuple occupies a fixed amount of space.

# 2. Dictionary Keys
locations: Dict[Tuple[int, int], str] = {(0, 0): 'Origin', (1, 2): 'Point A'}  # Using tuples as dictionary keys


# Time Complexity: O(1) - Average-case time complexity for dictionary operations (key lookup, insertion).
# Space Complexity: O(n) - Where n is the number of key-value pairs in the dictionary.

# 3. Function Return Values
def divide(x: int, y: int) -> Tuple[int, int]:
    return (x // y, x % y)  # Returns a tuple containing quotient and remainder


result: Tuple[int, int] = divide(10, 3)  # result will be (3, 1)
print(result)  # Output: (3, 1)
# Time Complexity: O(1) - Tuple creation and return is constant time.
# Space Complexity: O(1) - Tuple occupies a fixed amount of space.

# 4. Data Integrity
settings: Tuple[str, int, str] = ('high', 60, 'blue')  # Immutable settings
# Time Complexity: O(1) - Accessing tuple elements is constant time.
# Space Complexity: O(1) - Tuple occupies a fixed amount of space.

# 5. Unpacking and Multiple Assignments
a: int
b: int
c: int
a, b, c = (1, 2, 3)  # Unpacking a tuple into multiple variables
# Time Complexity: O(1) - Tuple unpacking is constant time.
# Space Complexity: O(1) - No additional space required.

# 6. Performance
# Tuples generally have better performance compared to lists due to their immutability.
# Time Complexity: O(1) - For most operations due to fixed size and immutable nature.
# Space Complexity: O(1) - Tuple occupies a fixed amount of space.

# 7. Structural Data
record: Tuple[str, int, str] = ('John', 28, 'Engineer')  # Fixed structure, like a database record
# Time Complexity: O(1) - Accessing tuple elements is constant time.
# Space Complexity: O(1) - Tuple occupies a fixed amount of space.

# 8. Data Integrity in Functional Programming
# Tuples are used in functional programming to ensure data immutability.
# Time Complexity: O(1) - Operations on tuples are generally constant time.
# Space Complexity: O(1) - Tuple occupies a fixed amount of space.
