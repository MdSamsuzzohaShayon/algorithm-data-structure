# BIG O NOTATION
# Definition: A theoretical measure of the execution of an algorithm, usually the time or memory needed, given the problem size n, which is usually the number of items. Informally, saying some equation f(n) = O(g(n)) means it is less than some constant multiple of g(n). The notation is read, "f of n is big oh of g of n".

# ORDER OF N - 0(n)
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers

numbers = [2,5,8,9]
print(get_squared_numbers(numbers))

# 1. KEEP FASTEST GROWING TERM
# 2. DROP CONSTANT


# FUNCTION THAT COMPLEXITY IS ORDER OF 1 - 0(1)
def find_first_pe(prices, eps, index):
    pe = prices(index)/eps[index]
    return pe;

# prices = [10, 12, 14]
# eps = [11, 13, 15]
# num = find_first_pe(prices, eps, 1)


# time = a * n^2 + b = 0(n^2)
numbers2 = [3,6,2,4,3,6,8,9]
for i in range(len(numbers2)):
    for j in range(i+1, len(numbers2)):
        if(numbers2[i] == numbers2[j]):
            print(str(numbers2[i]) + " is duplicate" )
            break
      
      
      
print("------------BREAK----------")
# time = a * n^ + b*n + c = 0(n^2)
duplicate = None
numbers3 = [3,6,2,4,3,6,8,9]
# n ^ 2   iterations
for i in range(len(numbers3)):
    for j in range(i+1, len(numbers3)):
        if(numbers3[i] == numbers3[j]):
            duplicate = numbers3[i]
            break

# n   iterations
for i in range(len(numbers3)):
    if numbers3[i] == duplicate:
        print(i)
        
        
        
        
# BINARY SEARCH
numbers4 = [4, 9, 15, 34, 57, 68, 91]
target = 68
# ITERATION 1  = n/2 = n / 2
# ITERATION 2 = (n / 2) / 2 = n / 2^2
# ITERATION 3 = (n / 2 ^2) / 2 = n / 2^3

# ITERATION K = n / 2^K
# 1 = n/2^k
# n = 2^k
# UNDERSCORE 2 MEANS 2 BELOW LOG
# log _2 n = K * LOG _2 2
# K= log n -> 0(log n)




