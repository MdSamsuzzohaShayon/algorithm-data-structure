"""
Tutorial: https://www.youtube.com/watch?v=ppmIOUIz4uI

Bubble sort is one of the simplest sorting algorithms used in data structures and algorithms (DSA). It repeatedly steps through the list to be sorted,
compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted. The algorithm is named
for the way smaller or larger elements "bubble" to the top of the list.

How Bubble Sort Works
    1. Compare Adjacent Elements: Start at the beginning of the list and compare the first two elements. If the first is greater than the second, swap them.
    2. Move to the Next Pair: Move to the next pair of elements and repeat the comparison and swap if necessary.
    3. Repeat for Each Pair: Continue this process for each pair of adjacent elements to the end of the list. After the first pass, the largest element will
       be in its correct position at the end of the list.
    4. Repeat the Entire Process: Repeat the entire process for the remaining elements, ignoring the last sorted elements each time.
    5. Continue Until Sorted: Continue this process until no swaps are needed, indicating that the list is sorted.

Example
Let's say we have the following list of numbers to sort in ascending order: [5, 3, 8, 4, 2]
First Pass:
    Compare 5 and 3, swap: [3, 5, 8, 4, 2]
    Compare 5 and 8, no swap: [3, 5, 8, 4, 2]
    Compare 8 and 4, swap: [3, 5, 4, 8, 2]
    Compare 8 and 2, swap: [3, 5, 4, 2, 8]

Second Pass:
    Compare 3 and 5, no swap: [3, 5, 4, 2, 8]
    Compare 5 and 4, swap: [3, 4, 5, 2, 8]
    Compare 5 and 2, swap: [3, 4, 2, 5, 8]
    8 is already in its correct position.

Third Pass:
    Compare 3 and 4, no swap: [3, 4, 2, 5, 8]
    Compare 4 and 2, swap: [3, 2, 4, 5, 8]
    5 and 8 are already in their correct positions.

Fourth Pass:
    Compare 3 and 2, swap: [2, 3, 4, 5, 8]
    Now the list is sorted: [2, 3, 4, 5, 8]

Big-O = O(n^2)
"""

from typing import List


def bubble_sort(elements: List[int]):
    """
    Sorts a list of integers using the bubble sort algorithm.

    Parameters:
    elements (List[int]): The list of integers to be sorted.
    """
    size = len(elements)  # Get the number of elements in the list
    for i in range(size - 1):  # Loop through each element except the last one
        swapped = False  # Flag to check if any elements were swapped during the iteration
        for j in range(size - 1 - i):  # Inner loop to compare adjacent elements
            # The '- i' part ensures we don't check already sorted elements at the end
            if elements[j] > elements[j + 1]:  # Compare adjacent elements
                # Swap if the current element is greater than the next element
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                swapped = True  # Set swapped to True as a swap has been made
        if not swapped:  # If no elements were swapped, the list is already sorted
            break  # Break out of the loop early


def bubble_sort_exercise(elements, key: str):
    """
    Sorts a list of dictionaries based on a specified key using the bubble sort algorithm.

    Parameters:
    elements (List[dict]): The list of dictionaries to be sorted.
    key (str): The key in the dictionary to sort by.
    """
    size = len(elements)  # Get the number of elements in the list
    for i in range(size - 1):  # Loop through each element except the last one
        swapped = False  # Flag to check if any elements were swapped during the iteration
        for j in range(size - 1 - i):  # Inner loop to compare adjacent elements
            # The '- i' part ensures we don't check already sorted elements at the end
            if elements[j][key] > elements[j + 1][key]:  # Compare adjacent elements based on the specified key
                # Swap if the current element's key is greater than the next element's key
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                swapped = True  # Set swapped to True as a swap has been made
        if not swapped:  # If no elements were swapped, the list is already sorted
            break  # Break out of the loop early


if __name__ == '__main__':
    # Example list of integers to be sorted
    elements: List[int] = [5, 9, 2, 1, 67, 34, 88, 34]
    bubble_sort(elements)  # Call the bubble_sort function to sort the list
    print(elements)  # Print the sorted list of integers

    # Example list of strings to be sorted alphabetically
    alpha_elements = ["Doctor Strange", "Hulk", "Iron Man", "Superman", "Batman", "Captain America"]
    bubble_sort(alpha_elements)  # Call the bubble_sort function to sort the list
    print(alpha_elements)  # Print the sorted list of strings

    # Example list of dictionaries to be sorted by different keys
    dict_elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    bubble_sort_exercise(dict_elements, 'device')  # Sort the list of dictionaries by 'device'
    print(dict_elements)  # Print the sorted list of dictionaries by 'device'

    bubble_sort_exercise(dict_elements, 'transaction_amount')  # Sort the list of dictionaries by 'transaction_amount'
    print(dict_elements)  # Print the sorted list of dictionaries by 'transaction_amount'

    bubble_sort_exercise(dict_elements, 'name')  # Sort the list of dictionaries by 'name'
    print(dict_elements)  # Print the sorted list of dictionaries by 'name'
