"""
The array-form of an integer num is an array representing its digits in left to right order.
For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

Example 1:
    Input: num = [1,2,0,0], k = 34
    Output: [1,2,3,4]
    Explanation: 1200 + 34 = 1234

Example 2:
    Input: num =  [2,7,4], k = 181
    Output: [4,5,5]
    Explanation: 274 + 181 = 455

Example 3:
    Input: num = [2,1,5], k = 806
    Output: [1,0,2,1]
    Explanation: 215 + 806 = 1021

LeetCode: https://leetcode.com/problems/add-to-array-form-of-integer/
YouTube Tutorial: https://www.youtube.com/watch?v=eBTZQt1TWfk&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=9
"""
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        i = 0
        while k:
            digit = k % 10
            if i < len(num):
                num[i] += digit
            else:
                num.append(digit)

            carry = num[i] // 10
            num[i] = num[i] % 10  # 12 % 10 = 2
            k = k // 10
            k += carry
            i += 1

        num.reverse()
        return num


sol = Solution()
print(sol.addToArrayForm(num=[1, 2, 0, 0], k=34)) # [1,2,3,4]
