"""
Tutorial: https://www.youtube.com/watch?v=ppmIOUIz4uI

Bubble sort is one of the simplest sorting algorithms used in data structures and algorithms (DSA). It repeatedly steps through the list to be sorted, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted. The algorithm is named for the way smaller or larger elements "bubble" to the top of the list.

How Bubble Sort Works
    1. Compare Adjacent Elements: Start at the beginning of the list and compare the first two elements. If the first is greater than the second, swap them.
    2. Move to the Next Pair: Move to the next pair of elements and repeat the comparison and swap if necessary.
    3. Repeat for Each Pair: Continue this process for each pair of adjacent elements to the end of the list. After the first pass, the largest element will be in its correct position at the end of the list.
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
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):  # by minusing i we are ignoring elements that is sorted
            if elements[j] > elements[j + 1]:
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                swapped = True
        if not swapped:
            break


def bubble_sort_exercise(elements, key: str):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j][key] > elements[j + 1][key]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    elements: List[int] = [5, 9, 2, 1, 67, 34, 88, 34]
    # sorted_elements: List[int] = [1, 2, 5, 9, 34, 34, 67, 88] # by using swapping we can prevent multiple loop

    bubble_sort(elements)
    print(elements)

    # alphabetic sorting
    alpha_elements = ["Doctor Strange", "Hulk", "Iron Man", "Superman", "Batman", "Captain America"]
    bubble_sort(alpha_elements)
    print(alpha_elements)

    dict_elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    bubble_sort_exercise(dict_elements, 'device')
    print(dict_elements)
    bubble_sort_exercise(dict_elements, 'transaction_amount')
    print(dict_elements)
    bubble_sort_exercise(dict_elements, 'name')
    print(dict_elements)

