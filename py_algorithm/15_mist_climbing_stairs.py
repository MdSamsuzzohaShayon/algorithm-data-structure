"""
Tutorial-1: https://youtu.be/NFJ3m9a1oJQ
Tutorial-2: https://www.youtube.com/watch?v=Y0lT9Fck7qI
Leetcode: https://leetcode.com/problems/climbing-stairs/description/
Leetcode 75 question solution: https://docs.google.com/spreadsheets/d/1A2PaQKcdwO_lwxz9bAnxXnIQayCouZP6d-ENrBz_NXc/edit?gid=0#gid=0

70. Climbing Stairs
Hint
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Climbing Stairs Problem Documentation
-------------------------------------

Problem Overview:
-----------------
- This is a classic dynamic programming problem.
- The problem can be found on LeetCode (Problem 70): https://leetcode.com/problems/climbing-stairs/description/
- You are given a staircase with 'n' steps, and you can climb either 1 step or 2 steps at a time.
- The task is to determine how many distinct ways you can climb to the top of the staircase.

Example Scenarios:
------------------
Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two distinct ways to climb to the top:
        1. Climb 1 step, then another 1 step.
        2. Climb 2 steps at once.

Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three distinct ways to climb to the top:
        1. Climb 1 step, then another 1 step, then another 1 step.
        2. Climb 1 step, then climb 2 steps.
        3. Climb 2 steps, then climb 1 step.

Constraints:
------------
- The number of steps, 'n', is a positive integer, and 1 <= n <= 45.

Understanding the Solution:
---------------------------
- The problem can be visualized as finding the number of distinct paths to reach the nth step.
- Let's break down the problem:
    - If you are on step 'i', you can reach there by either:
        1. Climbing from step 'i-1' by taking 1 step.
        2. Climbing from step 'i-2' by taking 2 steps.
    - Therefore, the number of ways to reach step 'i' is the sum of ways to reach step 'i-1' and step 'i-2'.
    - This leads to the relation:
        ways(i) = ways(i-1) + ways(i-2)
- This is analogous to the Fibonacci sequence, where each number is the sum of the previous two numbers.

Detailed Code Explanation:
--------------------------
- The solution is implemented in the class `Solution`, with the method `climbStairs`.
- The function takes an integer `n` representing the total number of steps.
- Two variables `one` and `two` are initialized to 1, representing the base cases for `ways(1)` and `ways(0)` respectively.
- The loop runs `n-1` times because we are calculating the number of ways to reach the nth step.
- Inside the loop:
    - `temp` stores the current value of `one` to update `two` later.
    - `one` is updated to the sum of `one` and `two`, which gives us the number of ways to reach the next step.
    - `two` is updated to the old value of `one` (stored in `temp`), representing the number of ways to reach the current step.
- Finally, the method returns `one`, which contains the number of distinct ways to reach the nth step.

Python Code Implementation:
---------------------------
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize two variables, both set to 1, representing the base cases.
        one, two = 1, 1

        # Loop through each step from 1 to n-1 to calculate the number of ways to reach step 'n'.
        for i in range(n-1):
            temp = one  # Store the current value of 'one' in 'temp'.
            one = one + two  # Update 'one' to be the sum of 'one' and 'two'.
            two = temp  # Update 'two' to be the previous value of 'one'.

        # Return the number of ways to reach the nth step.
        return one

"""
Test Cases:
-----------
Let's write some test cases to validate the solution.

Test Case 1:
    Input: n = 2
    Expected Output: 2
    Explanation: Two distinct ways: (1+1), (2)

Test Case 2:
    Input: n = 3
    Expected Output: 3
    Explanation: Three distinct ways: (1+1+1), (1+2), (2+1)

Test Case 3:
    Input: n = 5
    Expected Output: 8
    Explanation: Eight distinct ways: (1+1+1+1+1), (1+1+1+2), (1+1+2+1), (1+2+1+1), (2+1+1+1),
                                           (1+2+2), (2+1+2), (2+2+1)

Test Case 4:
    Input: n = 1
    Expected Output: 1
    Explanation: Only one way: (1)

"""

# Example usage of the Solution class to test the method
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    n = 2
    print(f"Test Case 1: n = {n}, Output: {solution.climbStairs(n)}, Expected: 2")

    # Test Case 2
    n = 3
    print(f"Test Case 2: n = {n}, Output: {solution.climbStairs(n)}, Expected: 3")

    # Test Case 3
    n = 5
    print(f"Test Case 3: n = {n}, Output: {solution.climbStairs(n)}, Expected: 8")

    # Test Case 4
    n = 1
    print(f"Test Case 4: n = {n}, Output: {solution.climbStairs(n)}, Expected: 1")
