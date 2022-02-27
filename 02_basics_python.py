print('\n UNPACK⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# UNPACKING - UNPACK THE N ITEMS OF A SEQUENCE INTO N VARIABLE
x = ['pig', 'cow', 'horse']
a, b, c = x
print(a, b, c)

print('\n LIST⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# LISTS - GENERAL PURPOSE, MOST WIDELY USED DATA STRUCTURE, GROW AND SHRINK SIZE AS NEEDED, SEQUENCE TYPE, SORTABLE
x = list()
y = ['a', 25, 'dog', 8.9]
tuple1 = (10, 20)
z = list(tuple1)
print(x, y, z)  # [] ['a', 25, 'dog', 8.9] [10, 20]

print('\n list comprehension⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
a = [m for m in range(8)]
print(a)  # [0, 1, 2, 3, 4, 5, 6, 7]
b = [i ** 2 for i in range(10) if i > 4]
print(b)  # [25, 36, 49, 64, 81] - 5 to 9 square in the list

print('\n DELETE/APPEND/EXTEND/INSERT/POP/REMOVE/REVERSE⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
x = [5, 8, 3, 6]
del (x[3])
print(x)  # [5, 8, 3]
x.append(32)  # [5, 8, 3, 32]
print(x)
y = [23, 81]
x.extend(y)
print(x)  # [5, 8, 3, 32, 23, 81]
x.insert(2, 17)  # INSERT AN ITEM AT A GIVEN INDEX
print(x)  # [5, 8, 17, 3, 32, 23, 81]
x.insert(3, ['new', 'new2'])  #
print(x)  # [5, 8, 17, ['new', 'new2'], 3, 32, 23, 81]
x.pop()  # POP LAST ITEM OFF THE LIST AND RETURNS ITEM
print(x)  # [5, 8, 17, ['new', 'new2'], 3, 32, 23]
x.remove(3)  # REMOVE FIRST INSTANCE OF AN ITEM
print(x)  # [5, 8, 17, ['new', 'new2'], 32, 23]
x.reverse()  # reverse the order of the list. it is an in-place sort, meaning it change the orginal list
print(x)  # [23, 32, ['new', 'new2'], 17, 8, 5]

print('\n SORT⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# SORT THE LIST IN PLACE
# SORTED(X) RETURNS A NEW SORTED LIST WITHOUT CHANGING THE ORGINAL LIST
# X.SORT() PUTS THE ITEMS OF X IN SORTED ORDER (SORTS IN PLACE )
x = [5, 6, 8, 3]
x.sort()  # ASCENDING
print(x)  # [3, 5, 6, 8]
x.sort(reverse=True)  # DESCENDING
print(x)  # [8, 6, 5, 3]

print('\n TUPLES⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# TUPLES - IMMUTABLE(CAN'T ADD/CHANGE) BUT MEMBER OBJECT MAY BE MUTABLE, USEFUL FOR FIXED DATA, FASTER THAN LISTS, SEQUENCE TYPE
x = ()
print(x)  # ()
x = (1, 2, 3, 6)
print(x)  # (1, 2, 3, 6)
x = 1, 3, 4, 6
print(x)  # (1, 3, 4, 6)
x = 2,  # COMMA INDICATE THAT ITS A TUPLE
print(x)  # (2,)
list1 = [2, 5, 6]
x = tuple(list1)
print(x, type(x))  # (2, 5, 6) <class 'tuple'>
# del(x[1]) # 'tuple' object doesn't support item deletion
# x[0] = 12 # 'tuple' object does not support item assignment

y = ([1, 2], 3)  # A TUPLE WHERE THE FIRST ITEM IS A LIST
del(y[0][1]) # DELETE ITEM FROM LIST IN A TUPLE
print(y) # ([1], 3)
y += (4,)
print(y) # ([1], 3, 4)



print('\n SETS⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# STORE NON-DUPLICATE ITEMS, VERY FAST ACCESS THAN LISTS, MATH SET OPS(UNION, INTERSECT), SETS ARE UNORDERED - CAN NOT ORDER
x = {3, 5, 3, 6}
print(x) # {3, 5, 6}
y = set()
print(y) # set()
list1 = [2,3,4 , 3]
z = set(list1)
print(z) # {2, 3, 4}
z.add(9)
print(z) # {9, 2, 3, 4}
z.remove(3)
print(z) # {9, 2, 4}
print(len(z)) # 3
print(5 in z) # False
print(z.pop(), z) # 9 {2, 4} - SINCE IT'S NOT ORDERED IT WILL POP RANDOM ITEM
z.clear()
print(z) # set()




