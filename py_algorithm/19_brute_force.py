"""
Tutorial: https://youtu.be/DKCbsiDBN6c
For any given problem, try all possible solution and pick up desired solution
Backtracking: Back tracking follows Depth First Search (DFS)
Branch and bound: Breath First Search (BFS)
State space tree


Example:
    There are 3 chairs and 3 student can sit there, 1 is  girl and 2 are boys. We can arrange them in 6 different ways means (3! = 6) using factorial formula

# Brute Force Algorithm

## Definition:
Brute force is a straightforward approach to solving a problem by trying all possible solutions and picking the desired one. This method is simple but often inefficient for large inputs.

## Characteristics:
- **Simple**: Easy to understand and implement.
- **Inefficient**: Can be impractical for large input sizes due to high time complexity.
- **Exhaustive**: Checks all possible solutions.

## Types of Search:
- **Backtracking**: Follows Depth First Search (DFS) principles.
- **Branch and Bound**: Follows Breadth First Search (BFS) principles.
- **State Space Tree**: Visual representation of the solution space.

## Real-Life Example:
Imagine you have a small lock with 3 digits, each ranging from 0 to 9. A brute force approach would try every possible combination until the correct one is found. This would involve 10 * 10 * 10 = 1000 attempts.

## Mathematical Example:
There are 3 chairs and 3 students (1 girl and 2 boys) who can sit there. We can arrange them in 6 different ways (3! = 6) using the factorial formula.

## Time Complexity:
- **String Matching**: O(n * m) where n is the length of the text and m is the length of the pattern.
- **Password Cracking**: O(c^n) where c is the number of possible characters and n is the length of the password.
- **Traveling Salesman Problem (TSP)**: O(n!) where n is the number of cities.

# Examples

## Example 1: Substring Search
"""


def brute_force_substring_search(text, pattern):
    n = len(text)  # Length of the text
    m = len(pattern)  # Length of the pattern

    # Iterate through each position in the text where the pattern could start
    for i in range(n - m + 1):
        j = 0
        # Check if the pattern matches the text starting from position i
        while j < m and text[i + j] == pattern[j]:
            j += 1
        # If we reached the end of the pattern, we found a match
        if j == m:
            return i  # Return the starting index of the match
    return -1  # No match found


text = "hello world"
pattern = "world"
result = brute_force_substring_search(text, pattern)
print(result)  # Output: 6 (the index of the match)

"""
## Example 2: Brute Force Password Cracking
"""


def brute_force_password_cracking(password):
    chars = 'abcdefghijklmnopqrstuvwxyz'  # Possible characters
    maxLength = len(password)

    def generate_combination(current_combination):
        if len(current_combination) > maxLength:
            return None
        if current_combination == password:
            return current_combination

        for char in chars:
            new_combination = current_combination + char
            result = generate_combination(new_combination)
            if result:
                return result
        return None

    return generate_combination('')


password = 'abc'
result = brute_force_password_cracking(password)
print(result)  # Output: 'abc' (the guessed password)
