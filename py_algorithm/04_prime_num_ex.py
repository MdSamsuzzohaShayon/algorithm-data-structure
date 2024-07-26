"""
Questions:
    What is a prime number?
    How can you determine if a number is prime?
    What is the time complexity of checking if a number is prime using trial division?
    What are some efficient algorithms for finding prime numbers?
    Can you identify scenarios where finding prime numbers might be useful in real life?
Tasks:
    Basic:
        Write a Python function to check if a number is prime using trial division.
        Write a Python function to generate a list of prime numbers up to a given number using the Sieve of Eratosthenes.
    Intermediate:
        Implement an optimized prime-checking function that reduces the number of division operations by checking only up to the square root of the number.
        Write a Python function that uses the Sieve of Eratosthenes to generate a list of prime numbers and then finds the sum of those primes.
    Advanced:
        Create a Python program that finds the largest prime factor of a very large number.
        Design a Python function that uses parallel processing to find prime numbers in a large range efficiently.
"""


# Example 1: Basic Prime Check using Trial Division
def is_prime_trial_division(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Example usage:
print(is_prime_trial_division(29))  # Output: True
# Explanation: This function checks if a number is prime by trying to divide it by every integer from 2 to n-1. If any division results in a remainder of 0, the number is not prime.

# Example 2: Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if primes[p]]

# Example usage:
print(sieve_of_eratosthenes(30))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# Explanation: This function generates a list of prime numbers up to a given limit using the Sieve of Eratosthenes, which marks non-prime numbers as False in a boolean array.

# Example 3: Optimized Prime Check
def is_prime_optimized(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage:
print(is_prime_optimized(29))  # Output: True
# Explanation: This function optimizes prime checking by only checking for divisibility up to the square root of n and skipping even numbers and multiples of 3.

# Example 4: Sum of Primes using Sieve of Eratosthenes
def sum_of_primes(limit):
    primes = sieve_of_eratosthenes(limit)
    return sum(primes)

# Example usage:
print(sum_of_primes(30))  # Output: 129
# Explanation: This function uses the Sieve of Eratosthenes to generate a list of prime numbers up to a given limit and then computes the sum of those primes.

# Example 5: Largest Prime Factor
def largest_prime_factor(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n if is_prime(n) else factor

# Example usage:
print(largest_prime_factor(13195))  # Output: 29
# Explanation: This function finds the largest prime factor of a given number by iteratively dividing the number by its smallest factor and checking if the resulting quotient is prime.

# Example 6: Parallel Prime Number Finder
from multiprocessing import Pool

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_range(start, end):
    return [num for num in range(start, end) if is_prime(num)]

def parallel_prime_finder(limit):
    num_processes = 4
    pool = Pool(processes=num_processes)
    step = limit // num_processes
    ranges = [(i * step + 1, (i + 1) * step) for i in range(num_processes)]
    ranges[-1] = (ranges[-1][0], limit)
    
    prime_lists = pool.starmap(find_primes_in_range, ranges)
    primes = [prime for sublist in prime_lists for prime in sublist]
    
    return primes

# Example usage:
print(parallel_prime_finder(30))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# Explanation: This function uses parallel processing to find prime numbers in a large range efficiently. It divides the range into chunks and processes them in parallel using multiprocessing.