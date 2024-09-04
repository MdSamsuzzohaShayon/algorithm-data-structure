from typing import List


# Majority element

def majority_element(nums: List[int]) -> int:
    res: int = 0
    count: int = 0
    for n in nums:
        if count == 0:
            res = n

        if n == res:
            count += 1
        else:
            count -= 1

    return res


print("Majority Element: ", majority_element([2, 2, 1, 9, 9, 9, 2, 2, 6, 6, 6]))