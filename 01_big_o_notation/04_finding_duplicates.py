# 0(n^2) 
# time = a * n^2 + b*n + c 
# WHEN VALUE OF N BECOME VERY LARGE B*N+C BECOME IRRELEVANT 
# 1. KEEP FASTEST GOING TERM 
# 2. DROP CONSTANT 
"""
BIG O REFERS TO BERY LARGE VALUE OF N, HENCE IF YOU HAVE A FUNCTION LIKE
EXAMPLE: N = 1000 
TIME = 5*1000^2 + 3*1000 + 20
TIME = 5000000 + 3020
"""

numbers = [ 3, 6, 2, 4, 3, 6, 8 , 9]
duplicate = None 
for i in range (len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            break

for i in range(len(numbers)):
    if numbers[i] == duplicate:
        print(i)