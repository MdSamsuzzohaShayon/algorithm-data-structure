"""
Tutorial: https://www.youtube.com/watch?v=UldZOLylez4
by using globals we are reassigning global variable
"""

from typing import List

pos: int = -1


def search(arr: List[int], n: int) -> bool:
    i: int = 0
    while i < len(arr):
        if arr[i] == n:
            globals()["pos"] = i
            return True
        i += 1
    return False


arr = [1, 3, 5, 7, 9, 6, 4]
n = 9

if search(arr, n):
    print("Found - ", pos + 1)
else:
    print("Not found")




# https://www.youtube.com/watch?v=QUdd1wzQpMc&t=173s
