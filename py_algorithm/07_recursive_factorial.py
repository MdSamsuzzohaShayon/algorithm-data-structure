"""
Recursive Factorial Function Tutorial

Factorial Definition:
n! = n * (n-1)!

Explanation:
- Factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
- It can be defined recursively, where:
  - The base case is 0! = 1.
  - For n > 0, n! = n * (n-1)!

Algorithm:
- If the number is 0, return 1 (base case).
- Otherwise, return the product of the number and the factorial of the number minus one (recursive case).

Tutorial Video: https://youtu.be/TqqQld6m6A0
"""


def factorial(num: int) -> int:
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
    num (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if num == 0:
        # Base case: 0! is defined as 1
        return 1
    # Recursive case: n! = n * (n-1)!
    return num * factorial(num - 1)


if __name__ == "__main__":
    # Example usage
    result = factorial(5)
    print(result)  # Output: 120
