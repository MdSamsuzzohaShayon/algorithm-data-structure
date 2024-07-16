# https://www.youtube.com/watch?v=lYCnThunjqY
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

