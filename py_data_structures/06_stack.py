from typing import List


# Last in first out (LIFO)
# Tutorial-1: https://youtu.be/stD5O9YnM04

# 3 primary operations: push, pop, and peek
# All of them has a time complexity of O(1) constant time

class Stack:
    def __init__(self):
        self.items: List[str] = []

    def push(self, element: str):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


# Last in first out (LIFO)
stack = Stack()
stack.push("One")
stack.push("Two")
stack.push("Three")
print("Remove: ", stack.pop())
print("Peek: ", stack.peek())
print(stack.items)

"""
Tutorial-1: https://youtu.be/stD5O9YnM04
Leetcode:  https://leetcode.com/problems/valid-parentheses/description/

20. Valid Parentheses
Easy
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.
"""

from typing import Dict, List


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if the input string `s` containing brackets is valid.

        A string is valid if:
        1. Every opening bracket has a corresponding closing bracket of the same type.
        2. Brackets are closed in the correct order.

        Args:
        s (str): The input string containing brackets.

        Returns:
        bool: True if the string is valid, False otherwise.
        """

        # Dictionary mapping each closing bracket to its corresponding opening bracket
        close_to_open: Dict[str, str] = {
            ")": "(",  # Closing bracket ')' matches opening bracket '('
            "}": "{",  # Closing bracket '}' matches opening bracket '{'
            "]": "[",  # Closing bracket ']' matches opening bracket '['
        }

        # Stack to keep track of unmatched opening brackets
        stack: List[str] = []

        # Iterate over each character in the input string
        for bracket in s:
            if bracket in close_to_open:
                # If the current character is a closing bracket

                if not stack:
                    # If the stack is empty, it means there's no corresponding opening bracket
                    return False

                # Pop the top element from the stack
                top: str = stack.pop()

                # Check if the popped element matches the expected opening bracket
                if close_to_open[bracket] != top:
                    # If it doesn't match, the string is invalid
                    return False
            else:
                # If the current character is an opening bracket
                stack.append(bracket)  # Push it onto the stack

        # After processing all characters, check if the stack is empty
        return not stack  # If stack is empty, all brackets are properly matched
        # If stack is not empty, some opening brackets did not have matching closing brackets


# Time and Space Complexity:
# Time Complexity: O(n)
# - Each character in the string is processed once, and each stack operation (push/pop) is O(1) on average.
# - Thus, the total time complexity is O(n), where n is the length of the string `s`.

# Space Complexity: O(n)
# - The space complexity is O(n) in the worst case, where n is the number of characters in the string `s`.
# - This is because, in the worst case, all characters could be opening brackets, and they would be stored in the stack.

# Test Cases
print("===== Leetcode 20 =====")
solution = Solution()

# Test Case 1: Valid parentheses
s = "()"
print(f"Input: '{s}' -> Output: {solution.isValid(s)}")
# Expected Output: True
# Explanation: Simple case with matching pair of parentheses.

# Test Case 2: Multiple valid pairs
s = "()[]{}"
print(f"Input: '{s}' -> Output: {solution.isValid(s)}")
# Expected Output: True
# Explanation: Multiple types of brackets, all properly matched.

# Test Case 3: Mismatched parentheses
s = "(]"
print(f"Input: '{s}' -> Output: {solution.isValid(s)}")
# Expected Output: False
# Explanation: Brackets are not properly matched.


"""
Tutorial-2: https://www.youtube.com/watch?v=qYlHrAKJfyA&list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo&index=2
Leetcode: https://leetcode.com/problems/simplify-path/description/

71. Simplify Path
Medium
Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path into its simplified canonical path.
In Unix-style file system context, a single period '.' signifies the current directory, a double period ".." denotes moving up one directory level, and multiple slashes such as "//" are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like "...") as valid names for files or directories.

The simplified canonical path should adhere to the following rules:
    It must start with a single slash '/'.
    Directories within the path should be separated by only one slash '/'.
    It should not end with a slash '/', unless it's the root directory.
    It should exclude any single or double periods used to denote current or parent directories.
    Return the new path.

Example 1:
    Input: path = "/home/"
    Output: "/home"
    Explanation:
    The trailing slash should be removed.

Example 2:
    Input: path = "/home//foo/"
    Output: "/home/foo"
    Explanation:
    Multiple consecutive slashes are replaced by a single one.

Example 3:
    Input: path = "/home/user/Documents/../Pictures"
    Output: "/home/user/Pictures"
    Explanation:
    A double period ".." refers to the directory up a level.

Example 4:
    Input: path = "/../"
    Output: "/"
    Explanation:
    Going one level up from the root directory is not possible.

Example 5:
    Input: path = "/.../a/../b/c/../d/./"
    Output: "/.../b/d"
    Explanation:
    "..." is a valid name for a directory in this problem.

Constraints:
    1 <= path.length <= 3000
    path consists of English letters, digits, period '.', slash '/' or '_'.
    path is a valid absolute Unix path.
"""

from typing import List


class Solution2:
    def simplifyPath(self, path: str) -> str:
        """
        Simplify the given Unix-style file system path to its canonical form.

        Args:
        path (str): The absolute path to be simplified.

        Returns:
        str: The simplified canonical path.
        """

        # Stack to keep track of directories
        stack: List[str] = []

        # Variable to accumulate characters of the current directory or file name
        curr: str = ""

        # Iterate over each character in the path, plus an extra slash to process the last directory/file
        for c in path + "/":
            if c == "/":
                if curr == "..":
                    # If current name is "..", pop from stack to go up one directory level
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    # If current name is not empty or "." (current directory), add it to stack
                    stack.append(curr)
                # Reset current name for next segment
                curr = ""
            else:
                # Accumulate characters for the current directory or file name
                curr += c

        # Join all directories with a single slash and prepend with a leading slash
        return "/" + "/".join(stack)


# Time and Space Complexity:
# Time Complexity: O(n)
# - We traverse the input string once and perform operations on the stack which are O(1) on average.
# - Thus, the total time complexity is O(n), where n is the length of the input string `path`.

# Space Complexity: O(n)
# - In the worst case, where the path has no ".." or ".", all directories could be stored in the stack.
# - Hence, the space complexity is O(n), where n is the number of directories in the simplified path.

# Test Cases
solution2 = Solution2()
print("===== Stack 2 =====")

# Test Case 1: Trailing slash should be removed
path = "/home/"
print(f"Input: '{path}' -> Output: '{solution2.simplifyPath(path)}'")
# Expected Output: "/home"

# Test Case 2: Multiple consecutive slashes should be replaced by a single one
path = "/home//foo/"
print(f"Input: '{path}' -> Output: '{solution2.simplifyPath(path)}'")
# Expected Output: "/home/foo"

# Test Case 3: Double period ".." refers to the directory up a level
path = "/home/user/Documents/../Pictures"
print(f"Input: '{path}' -> Output: '{solution2.simplifyPath(path)}'")
# Expected Output: "/home/user/Pictures"

# Test Case 4: Going one level up from the root directory
path = "/../"
print(f"Input: '{path}' -> Output: '{solution2.simplifyPath(path)}'")
# Expected Output: "/"

# Test Case 5: Valid names for directories with mixed periods and slashes
path = "/.../a/../b/c/../d/./"
print(f"Input: '{path}' -> Output: '{solution2.simplifyPath(path)}'")
# Expected Output: "/.../b/d"


