# 04:08:00 - explanation
# 04:15:00 - start coding

import random
import sys



# try:
#     f = open('./utils/number-5.txt', encoding='utf-8')
#     print(f.read())
# except Exception as e:
#     print(3)
# finally:
#     f.close()

num_list = [3, 8, 6, 2, 10]


def is_sorted(values):
    for index in range(len(values) - 1):
        if (values[index]) > values[index + 1]:
            return False
    return True


"""
A imperfect sorting algorithm that randomizes the order of a list and 
then checks to see if it happens to be sorted
random attempts for search an item
Bogo sort does not make any progress toward a solution with each pass
It could generate a list where just one value is out of order
In next attempt it could generate a list where all the elements are out of order again
"""
def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values

print(bogo_sort(num_list))
