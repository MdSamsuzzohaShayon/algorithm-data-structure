"""
Array or list is a data structure that can host a collection of values.
Array can contain a mix of different data types. String, boolean, number, event object can be stored in the List
Arrays are resizeable. Do not need to declare array size before creating it
In Python, lists are also zero-indexed, meaning the first element of a list has an index of 0. Additionally, like JavaScript arrays, Python lists maintain the insertion order. 
Arrays are iterables. It can be used with loop
"""

arr = [1, 2, 3, 'Shayon'] # List can contains mixed data types
arr.append(4)
arr.insert(0, 20)

for a in arr:
    print(a)

arr.pop()
arr.pop(0)

print("===================")

for a in arr:
    print(a)


"""
List/ Array - Big-O time complexity

arr.append(4) - O(1)
Appending an element to the end of the list. The average time complexity of the append operation is O(1), but in the worst case (when the list needs to be resized), it can be O(n).

arr.insert(0, 20) - O(n)
Inserting an element at the beginning of the list. This operation has a time complexity of O(n) because all existing elements need to be shifted to make room for the new element.

arr.pop() - O(1)
Removing the last element from the list. The average time complexity of the pop operation is O(1).

arr.pop(0) - O(n)
Removing the first element from the list. This operation has a time complexity of O(n) because, after removing the element, all remaining elements need to be shifted to fill the gap.
"""