"""
Tutorial: https://www.youtube.com/watch?v=x2F2BIAB-bs
F0 = 0
F1 = 1
Fn = Fn-2 + Fn-1
"""

def fib(n: int)-> int:
    if n < 2:
        return n
    return fib(n - 2) + fib(n-1)


print(fib(8))

for n in range(0, 16):
    print(fib(n))