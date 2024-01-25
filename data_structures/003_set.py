"""
A set is a data structure that can hold a collection of value. The values however must be unique.
Set can contain a mix of different data types. You can store strings, booleans, numbers or even objects all in the same set
Sets are dynamically sized. You do not have to declare the size of a set before creating it.
Set do not maintain an insertion order
Sets are iterables that can be used with for of loop
https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

Set VS Array/List
arrays can contain duplicate values whereas sets can not
Insertion order is maintained in arrays but it is not the case in sets
Searching and deleting an element in the set is faster compared to arrays

https://www.youtube.com/watch?v=vfPd6_H7W4Q&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=39
"""

new_set = set([3, 4, 4, 5, 6, 7])
new_set.add(8)
for num in new_set:
    print(num)

print("Has 4 in the set -> ",4 in new_set)
new_set.remove(6)
print("Removing 6 from set -> ",new_set)
print(len(new_set))

new_set.clear()
print("After clearing everything from set-> ",new_set)

"""
new_set.add(8) - O(1)
Adding an element to a set has an average time complexity of O(1). In most cases, it's a constant time operation because sets are implemented as hash tables.

new_set.clear() - O(n)
Clearing a set, i.e., removing all elements from the set, has a time complexity of O(n), where n is the number of elements in the set.
"""




