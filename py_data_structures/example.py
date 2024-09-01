# Recursive Solution (without DP)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Dynamic Programming Solution
def fibonacci(n):
    # Create a table to store results of subproblems
    dp = [0] * (n + 1)
    
    # Base cases
    if n >= 1:
        dp[1] = 1
    
    # Fill the table iteratively
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]