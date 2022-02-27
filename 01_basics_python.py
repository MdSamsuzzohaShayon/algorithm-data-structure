# ACCESSING ANY ITEM IN THE SEQUENCE USING ITS INDEX

print('\n SLICING⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# SLICING - SLICE OUT SUBSTRING, SUBLISTS, SUBTUPLES USING INDEX
x = "computer"
print(x[1:4]) # omp
print(x[1:6:2]) # opt - [START : END + 1 : STEP]
print(x[3:]) # puter
print(x[:3]) # com
print(x[-1]) # r
print(x[-3:]) # ter
print(x[:-2]) # comput



print('\n ADDING / CONCATENATING⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# ADDING / CONCATENATING - COMBINE 2 SEQUENCES OF THE OF THE SAME TYPE
# STRING
x = 'horse' + 'shoe'
print(x) # horseshoe

# LIST
y = ['pig', 'cow'] + ['horse']
print(y) # ['pig', 'cow', 'horse']

# TOUPLE
z = ('Kevin', 'Niklas', "Jenny") + ('Craig', )
print(z) # ('Kevin', 'Niklas', 'Jenny', 'Craig')


print('\n MULTIPLY⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# MULTIPLY  - MULTIPLY  A SEQUENCE
x = "bug" * 3
print(x) # bugbugbug

# LIST
y = [8, 5] * 3
print(y) # [8, 5, 8, 5, 8, 5]

z = (2, 4) * 3
print(z) # (2, 4, 2, 4, 2, 4)


print('\n CHECKING MEMBERSHIP⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# CHECKING MEMBERSHIP - TEST WHETHER AN ITEM IS OR IS NOT IN A SEQUENCE
x = 'bug'
print('u' in x) # TRUE

y = ['pig', 'cow', 'horse']
print('horse' not in y) # FALSE

z = ('Kevin', 'Niklas', "Jenny", 'Craig' )
print('Kevin ' in z) # FALSE


print('\n ITERATING⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# ITERATING - ITERATING THROUGH THE ITEMS IN A SEQUENCE
x = [7, 8 , 3]
for item in x:
    print(item)

y = x
for index, item in enumerate(y):
    print(index, item)


print('\n NUMBER OF ITEMS⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# NUMBER OF ITEMS - count the number of items in a sequence
x = 'BUG'
print(len(x))

y = ['pig', 'cow', 'horse']
print(len(y))

z = ('Kevin', 'Niklas', "Jenny", 'Craig' )
print(len(z))





print('\n MINIMUM⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# MINIMUM - FIND THE MINIMUM ITEM IN A SEQUENCE LEXICOGRAPHICALLY ALPHA OR NUMERIC TYPES, BUT CAN NOT MIX TYPES

x = 'BUG'
print(min(x))  # B

y = ['pig', 'cow', 'horse']
print(min(y)) # cow

z = ('Kevin', 'Niklas', "Jenny", 'Craig' )
print(min(z)) # Craig


print('\n MAXIMUM⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# MAXIMUM - FIND THE MAXIMUM ITEM IN A SEQUENCE LEXICOGRAPHICALLY ALPHA OR NUMERIC TYPES, BUT CAN NOT MIX TYPES

x = 'BUG'
print(max(x))  # U

y = ['pig', 'cow', 'horse']
print(max(y)) # pig

z = ('Kevin', 'Niklas', "Jenny", 'Craig' )
print(max(z)) # Niklas


print('\n SUM⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# SUM - FIND SUM OF ITEMS IN A SEQUENCE, ENTIRE SEQUENCE MUST BE NUMERIC.

# string -> error
# x = [5, 7, 'bug']
# print(sum(x)) #ypeError: unsupported operand type(s) for +: 'int' and 'str'

y = [2,3,5,7,12]
print(sum(y)) # 29
print(sum(y[-2:])) # 19

z = (50, 4, 7, 19)
print(sum(z)) # 80

print('\n SORTING⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# SORTING - RETURNS A NEW LIST OF ITEMS IN SORTED ORDER, DOES NOT CHANGE THE ORGINAL LIST
x = 'bug'
print(sorted(x)) # ['b', 'g', 'u']

y = ['pig', 'cow', 'horse']
print(sorted(y)) # ['cow', 'horse', 'pig']

z = ('Kevin', 'Niklas', "Jenny", 'Craig' )
print(sorted(z)) # ['Craig', 'Jenny', 'Kevin', 'Niklas']

# SORTING BY SECOND LETTER
# ADD A KEY PARAMETER AND A LAMDA FUNCTION TO RETURN THE SECOND CHARECTER (THE WORD KEY HERE IS A DEFINED PARAMETER NAME, K IS AN ARBITRARY VARIABLE NAME)
z = ('Kevin', 'Niklas', "Jenny", 'Craig' )
print(sorted(z, key=lambda k:k[1])) # ['Kevin', 'Jenny', 'Niklas', 'Craig']


print('\n COUNT⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# count(item) - returns count of an item
x = 'hippo'
print(x.count('p')) # 2

y = ['pig', 'cow', 'horse']
print(y.count('pig')) # 1

z = ('Kevin', 'Niklas', "Jenny", 'Craig', 'Jenny')
print(z.count("Jenny")) # 2

print('\n INDEX⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹🍮🍮🍮⟹⟹⟹⟹⟹⟹⟹⟹⟹⟹ \n')
# INDEX(ITEM) - RETURNS THE INDEX OF THE FIRST OCCURENCE OF AN ITEM
x = 'hippo'
print(x.index('p')) # 2

y = ['pig', 'cow', 'horse']
print(y.index('pig')) # 0

z = ('Kevin', 'Niklas', "Jenny", 'Craig', 'Jenny')
print(z.index("Jenny")) # 2


























