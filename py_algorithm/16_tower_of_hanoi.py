"""
Tutorial-1: https://youtu.be/rf6uf3jNjbo


Tower of Hanoi Problem Documentation
------------------------------------

Problem Overview:
-----------------
- The Tower of Hanoi is a classic problem in mathematics and computer science.
- The problem involves three rods and a number of disks of different sizes that can slide onto any rod.
- The puzzle starts with the disks stacked in ascending order of size on one rod, the smallest at the top.
- The objective is to move the entire stack to another rod, obeying the following rules:
    1. Only one disk can be moved at a time.
    2. Each move consists of taking the top disk from one stack and placing it on top of another stack or on an empty rod.
    3. No disk may be placed on top of a smaller disk.

Problem Definition:
-------------------
- The Tower of Hanoi puzzle can be solved recursively with the following steps:
    1. Move the top n-1 disks from the source rod to the auxiliary rod.
    2. Move the nth (largest) disk from the source rod to the destination rod.
    3. Move the n-1 disks from the auxiliary rod to the destination rod.

Example Scenario:
-----------------
- Consider the case with 3 disks (n = 3) and rods named 'A', 'B', and 'C':
    1. Move disk 1 from A to C.
    2. Move disk 2 from A to B.
    3. Move disk 1 from C to B.
    4. Move disk 3 from A to C.
    5. Move disk 1 from B to A.
    6. Move disk 2 from B to C.
    7. Move disk 1 from A to C.

- The minimum number of moves required to solve the Tower of Hanoi problem with n disks is 2^n - 1.

Understanding the Recursive Solution:
-------------------------------------
- The problem is solved recursively by breaking it down into smaller subproblems.
- The base case occurs when there is only one disk (n = 1), which can be directly moved to the destination rod.
- For more than one disk, the function recursively solves the problem for n-1 disks, then moves the largest disk, and finally solves the problem for the remaining n-1 disks.

Detailed Code Explanation:
--------------------------
- The solution is implemented in the function `tower_of_hanoi`, which prints the sequence of moves required to solve the puzzle.
- The function takes four arguments:
    1. `n`: The number of disks.
    2. `source`: The name of the source rod.
    3. `target`: The name of the destination rod.
    4. `auxiliary`: The name of the auxiliary rod.

- The base case occurs when `n = 1`, in which case the function prints the move from the source rod to the target rod.
- If `n > 1`, the function recursively moves the top n-1 disks to the auxiliary rod, then moves the nth disk to the target rod, and finally moves the n-1 disks from the auxiliary rod to the target rod.

Python Code Implementation:
---------------------------
"""


def tower_of_hanoi(n: int, source: str, target: str, auxiliary: str):
    """
    Solves the Tower of Hanoi problem for n disks and prints each move.

    Parameters:
    -----------
    n : int
        The number of disks to move.
    source : str
        The name of the source rod.
    target : str
        The name of the target rod.
    auxiliary : str
        The name of the auxiliary rod.

    Returns:
    --------
    None
    """
    # Base case: If only one disk, move it directly from source to target.
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Step 1: Move the top n-1 disks from source to auxiliary, using target as auxiliary.
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # Step 2: Move the nth disk (largest disk) from source to target.
    print(f"Move disk {n} from {source} to {target}")

    # Step 3: Move the n-1 disks from auxiliary to target, using source as auxiliary.
    tower_of_hanoi(n - 1, auxiliary, target, source)


"""
Test Cases:
-----------
Let's test the `tower_of_hanoi` function with different numbers of disks.

Test Case 1:
    Input: n = 2
    Expected Output:
        Move disk 1 from A to B
        Move disk 2 from A to C
        Move disk 1 from B to C

Test Case 2:
    Input: n = 3
    Expected Output:
        Move disk 1 from A to C
        Move disk 2 from A to B
        Move disk 1 from C to B
        Move disk 3 from A to C
        Move disk 1 from B to A
        Move disk 2 from B to C
        Move disk 1 from A to C

Test Case 3:
    Input: n = 4
    Expected Output:
        Move disk 1 from A to B
        Move disk 2 from A to C
        Move disk 1 from B to C
        Move disk 3 from A to B
        Move disk 1 from C to A
        Move disk 2 from C to B
        Move disk 1 from A to B
        Move disk 4 from A to C
        Move disk 1 from B to C
        Move disk 2 from B to A
        Move disk 1 from C to A
        Move disk 3 from B to C
        Move disk 1 from A to B
        Move disk 2 from A to C
        Move disk 1 from B to C

"""

# Example usage of the tower_of_hanoi function to solve the puzzle
if __name__ == "__main__":
    # Test Case 1: Tower of Hanoi with 2 disks
    print("Test Case 1: n = 2")
    tower_of_hanoi(2, 'A', 'C', 'B')

    # Test Case 2: Tower of Hanoi with 3 disks
    print("\nTest Case 2: n = 3")
    tower_of_hanoi(3, 'A', 'C', 'B')

    # Test Case 3: Tower of Hanoi with 4 disks
    print("\nTest Case 3: n = 4")
    tower_of_hanoi(4, 'A', 'C', 'B')

"""
Time Complexity:
----------------
- The time complexity of the Tower of Hanoi problem is O(2^n).
- Each move involves a constant amount of work, and there are 2^n - 1 moves.

Space Complexity:
-----------------
- The space complexity is O(n), where 'n' is the number of disks.
- This is due to the recursive call stack, where each level of recursion requires space for storing function parameters.

Conclusion:
-----------
The Tower of Hanoi is an excellent example of a problem that can be solved using recursion.
It demonstrates how complex problems can be broken down into smaller, manageable subproblems.
The recursive solution is both elegant and efficient for this classic puzzle.
"""
