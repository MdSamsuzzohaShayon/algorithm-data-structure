def merge_sort(list):
    """
    Sortes a list in ascending order
    :param list: sort the list we pass in
    :return: a new sorted list
    Merge sort has 3 main steps
        1. Divide: and find the midpoint and divide into sublist
        2. Conquer: Recursively sort the sublist created in previous step
        3. Combine: Merge the sorted sublist created in previous step

    In conclusion the top level function Takes O(kn log n) time for overall sorting process which is much more expensive for time complexity
    To fix this make it O(n log n)

    Space complexity - merge sort algorithm take linear space and this is weired

    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    :param list: divide the unsorted list at midpoint into sublist
    :return: two sublist return - left and right
    takes overall logarithmic O(log n) time
    Slicing operation in python is not constant time operation. In fact has a runtime of big O of k where k represents the slice size
    There are two version of binary search in python
        1. recursive - list slicing with every recursion but we achieve the same result using an iterative approach without using list slicing
        2. Iterative -
    """
    mid = len(list) // 2  # https://peps.python.org/pep-0238/
    left = list[:mid]
    right = list[mid:]
    return left, right


def merge(left, right):
    """
    Merge two lists (arrays), sorting tiem in the process
    :return: A new merged list
    Sort the value in both list
    for list of size n we always need n number of merge operations to get back from single element list to a merge list
    Runs overall linear O(n) time because that's an n number of merge steps multiplied by log n number of splits of the original list
    """
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


sortable_list = [34, 78, 12, 31, 42, 23, 62, 19]
l = merge_sort(sortable_list)
print(l)


def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


print(verify_sorted(sortable_list))
print(verify_sorted(l))
