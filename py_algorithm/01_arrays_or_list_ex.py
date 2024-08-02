"""
Questions
    Basic:
        What is an array/list, and how is it different from other data structures?
        How do you access elements in a list by their index?
        How do you add an element to the end of a list?
    Intermediate:
        How do you remove an element from a list by its value?
        How can you find the maximum and minimum values in a list?
        How do you concatenate two lists?
    Advanced:
        How can you implement a dynamic array that automatically resizes when it reaches its capacity?
        How do you reverse a list in place?
        How can you remove duplicates from a list efficiently?


Tasks
    Basic:
        Create a list of the first 10 natural numbers.
        Write a function that takes a list and an element as input and returns the index of the element in the list.
        Write a function to add a given element to the end of a list.
    Intermediate:
        Write a function that takes a list and an element as input and removes the first occurrence of the element from the list.
        Write a function to find the second largest number in a list.
        Write a function that merges two sorted lists into one sorted list.
    Advanced:
        Implement a dynamic array class that supports basic operations (e.g., append, remove) and resizes automatically.
        Write a function to reverse a list in place without using any extra space.
        Write a function to remove duplicates from a list while maintaining the order of elements.

"""



# Basic Example: Accessing Elements in a List

# Creating a list of the first 10 natural numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Accessing elements by index
print(numbers[0])  # Output: 1
print(numbers[9])  # Output: 10

# Adding an element to the end of the list
numbers.append(11)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# Intermediate Example: Removing an Element by Value
# Function to remove the first occurrence of an element
def remove_element(lst, value):
    if value in lst:
        lst.remove(value)
    return lst

# Example usage
numbers = [1, 2, 3, 4, 3, 5]
print(remove_element(numbers, 3))  # Output: [1, 2, 4, 3, 5]
# Advanced Example: Reversing a List In-Place
# Function to reverse a list in place
def reverse_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

# Example usage
numbers = [1, 2, 3, 4, 5]
print(reverse_list(numbers))  # Output: [5, 4, 3, 2, 1]