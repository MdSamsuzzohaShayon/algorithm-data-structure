# Create a few questions with ChatGPT and answer them as exercise
# Find and complete some tasks of fibonacci sequence
# Work with both Iterative and Recursive fibonacci sequence
# Remember first 2 numbers for fibonacci sequence are 0 and 1

from typing import List

# Iterative
def fib_ite(n: int)-> int:
    seq: List[int] = [0, 1]
    for n in range(2, n):
        # seq[n] = seq[n-1] + seq[n-2]
        seq.append(seq[n-1] + seq[n-2])
    return seq

print(fib_ite(10))



# Recursive
def fib_rec(n: int):
    pass
