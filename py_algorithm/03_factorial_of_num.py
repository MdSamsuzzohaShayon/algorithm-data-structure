# https://www.youtube.com/watch?v=6xpwQn-TqAQ&t=8s

"""
Factorial
Shows like this 5! means 5 factorial
5! Factorial can be calculated like:
    5! = 5 * 4 * 3 * 2 * 1 = 120

Formula
    n! = n*(n-1)!

Factorial of 0 is 1
"""


# Loop
def factorial(n: int) -> int:
    fac: int = 1
    for i in range(n):
        fac *= i + 1
    return fac


print("Factorial of 0: ", factorial(0))
print("Factorial of 1: ", factorial(1))
print("Factorial of 4: ", factorial(4))
print("Factorial of 5: ", factorial(5))


# Recursive factorial tutorial - https://youtu.be/UAqnxAiPKtU?list=PLztBpqftvzxUWTfxzaICDNe4UCAQW6sWB
def recursive_factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * recursive_factorial(n - 1)


print("Recursive Factorial of 5: ", recursive_factorial(5))


# https://www.youtube.com/watch?v=gfhtaP5Wq7M
def fact(n: int) -> int:
    f = 1
    for i in range(1, n + 1):
        f = f * i

    return f


print("Factorial of 5: ", fact(5))
