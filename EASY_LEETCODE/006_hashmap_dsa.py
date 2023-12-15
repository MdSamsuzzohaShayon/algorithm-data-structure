"""
YouTube: https://www.youtube.com/watch?v=RcZsTI5h0kg

In Python, a HashMap is implemented using a data structure called a dictionary, which is part of the Python standard library.
The dictionary is a collection of key-value pairs, where each key must be unique. It is also known as an associative array, map, or hash map in other programming languages.
A hashmap is implemented using an underlying array. The array is used as a bucket to store linked lists or other data structures containing key-value pairs.

Collisions: (two keys hashing to the same index) are handled by techniques such as chaining or open addressing.

A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.
Docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

A mapping object maps hashable values to arbitrary objects. Mappings are mutable objects. There is currently only one standard mapping type, the dictionary.
Mapping: https://docs.python.org/3/library/stdtypes.html#typesmapping

"""


# LeetCode Problem - https://leetcode.com/problems/group-anagrams/

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example-1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
Example-2: 
    Input: strs = [""]
    Output: [[""]]
    
Example-3: 
    Input: strs = ["a"]
    Output: [["a"]]
"""
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str])->List[List[str]]:
        anagram_map = defaultdict(list) # By setting default dict it will initialize with empty array
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s)) # make immutable by touple
            anagram_map[sorted_s].append(s)

        for val in anagram_map.values():
            result.append(val)

        return result


sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))