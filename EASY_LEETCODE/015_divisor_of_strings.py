"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

Example 2:
    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

Example 3:
    Input: str1 = "LEET", str2 = "CODE"
    Output: ""

Constraints:
    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.

LeetCode: https://leetcode.com/problems/greatest-common-divisor-of-strings/
YouTube Tutorial: https://www.youtube.com/watch?v=i5I_wrbUdzM&list=PLQpVsaqBj4RIJdYW6Y-iAswxCZeocfoRW&index=14
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            if len1 % 1 or len2 % 1:
                return False

            f1, f2 = len1 // 1, len2 // 1
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(len1, len2)):
            if isDivisor(str1[:1]):
                return str1[:1]

        return ""
