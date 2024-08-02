# https://www.youtube.com/watch?v=lYCnThunjqY
"""
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. In other words, a prime number is a number that can only be divided evenly (without leaving a remainder) by 1 and the number itself.
For example:
    2 is a prime number because its only divisors are 1 and 2.
    3 is a prime number because its only divisors are 1 and 3.
    5 is a prime number because its only divisors are 1 and 5.
Numbers that have more than two positive divisors are called composite numbers. For instance, 4 is a composite number because it can be divided by 1, 2, and 4.
"""
from typing import List
print("========= PRIME NUMBER PROGRAM =========")
print("\n Options: ")
print("     1. Check if number is prime")
print("     2. List prime numbers in range")

option: str = input("Enter 1 or 2")

# if option == "1":
#     number  = int(input("Enter a number greater than 1: "))
#     prime = True
#     for n in range(2, number):
#         if number % n == 0:
#             prime = False
#             print(f"{number} is not prime")
#             break
#     if prime:
#         print(f"{number} is prime")
# else:
#     number  = int(input("Enter a number greater than 1: "))


if option == "1":
    number = int(input("Enter a number greater than 1: "))
    for n in range(2, number):
        if number % n == 0:
            prime: bool = False
            print(f"{number} is not prime")
            break
    else:
        print(f"{number} is prime")
elif option == '2':
    print("Choose a range (from x through y)")
    x_val: int = int(input("Enter x (greater than 1): "))
    y_val: int = int(input("Enter y: "))
    list_prime_num: List[int] = []
    for num in range(x_val, y_val + 1):
        for n in range(2, num):
            if num % n == 0:
                break
        else:
            list_prime_num.append(num)

    print(f"Prime numbers from {x_val} through {y_val}")
    for prime in list_prime_num:
        print(f"{prime}, ", end="")