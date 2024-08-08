from typing import List
import math

"""
Theoretical Questions with Answers and Practical Tasks on Counting Prime Numbers in DSA

Theoretical Questions

1. What is a Prime Number?
   - **Question:** Define a prime number and explain its properties.
   - **Answer:** A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
   This means a prime number has exactly two distinct positive divisors: 1 and the number itself. For example, 2, 3, 5, and 7 are prime numbers.

2. Why is the number 1 not considered a prime number?
   - **Question:** Why is the number 1 not considered a prime number?
   - **Answer:** The number 1 is not considered a prime number because it has only one positive divisor (itself). By definition, prime numbers must have exactly two distinct 
   positive divisors, and 1 does not meet this criterion.

3. Describe the Naive Algorithm for Prime Checking.
   - **Question:** Describe the naive algorithm to check if a given number `n` is prime.
   - **Answer:** The naive algorithm to check if a number `n` is prime involves iterating through all numbers from 2 to `n-1` and checking if any of them divide 
   `n` without a remainder. If any number does, `n` is not prime. If none do, `n` is prime. The time complexity of this algorithm is O(n).

4. Optimizing Prime Checking
   - **Question:** How can the naive prime-checking algorithm be optimized for larger values of `n`?
   - **Answer:** The naive algorithm can be optimized by checking divisors only up to the square root of `n`, rather than up to `n-1`. 
   If `n` is divisible by any number in this range, it is not prime. This reduces the time complexity to O(√n).

5. Explain the Sieve of Eratosthenes.
   - **Question:** What is the Sieve of Eratosthenes, and how does it work?
   - **Answer:** The Sieve of Eratosthenes is an efficient algorithm for finding all prime numbers up to a given limit `n`. 
   It works by iteratively marking the multiples of each prime number starting from 2. The numbers that remain unmarked at the end of the process are primes. 
   The time complexity of the Sieve of Eratosthenes is O(n log log n).

6. Prime Counting Function (π(x))
   - **Question:** What is the prime counting function π(x)?
   - **Answer:** The prime counting function π(x) denotes the number of prime numbers less than or equal to `x`. It is a significant function in number theory, 
   particularly in the study of the distribution of prime numbers.

"""

"""
Practical Tasks

1. Task: Naive Prime Checking
   - **Description:** Implement a function `is_prime(n: int) -> bool` that checks if a given number `n` is prime using the naive method.
   - **Example:** `is_prime(29)` should return `True`.
   - **Hint:** Iterate through all numbers from 2 to `n-1` and check divisibility.
"""


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


"""
2. Task: Optimized Prime Checking
   - **Description:** Implement an optimized version of the prime-checking function `is_prime_optimized(n: int) -> bool` by only checking divisibility up to the square root of `n`.
   - **Example:** `is_prime_optimized(29)` should return `True`.
   - **Hint:** Use the `math.sqrt()` function to find the square root of `n` and iterate only up to this value.
"""


def is_prime_optimized(n: int) -> bool:
    if n <= 1:
        return False

    # for i in range(2, math.sqrt(n)):
    #     if n % i == 0:
    #         return False
    i = 2
    while i < math.sqrt(n):
        if n % i == 0:
            return False
        i += 1

    return True


"""
3. Task: Sieve of Eratosthenes Implementation
   - **Description:** Implement the Sieve of Eratosthenes to find all prime numbers up to a given number `n`.
   - **Example:** `sieve_of_eratosthenes(50)` should return `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]`.
   - **Hint:** Create a boolean array to mark non-prime numbers and iterate through it.

4. Task: Counting Primes in a Range
   - **Description:** Write a function `count_primes_in_range(start: int, end: int) -> int` that counts the number of prime numbers in a given range `[start, end]`.
   - **Example:** `count_primes_in_range(10, 30)` should return `6`.
   - **Hint:** Use the Sieve of Eratosthenes to precompute primes and then count them within the specified range.

5. Task: Prime Counting Function π(x)
   - **Description:** Implement a function `prime_counting_function(x: int) -> int` that returns the number of prime numbers less than or equal to `x`.
   - **Example:** `prime_counting_function(10)` should return `4`.
   - **Hint:** Use a prime-checking method or the Sieve of Eratosthenes to count primes up to `x`.

6. Task: Store and Retrieve Primes Using a Set
   - **Description:** Implement a function `generate_prime_set(n: int) -> set` that generates a set of all prime numbers up to `n` for quick lookup.
   - **Example:** `prime_set = generate_prime_set(50)` should allow `29 in prime_set` to return `True`.
   - **Hint:** Use the Sieve of Eratosthenes to generate the primes and store them in a set.
"""
