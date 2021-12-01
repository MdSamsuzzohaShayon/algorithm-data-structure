# 0(n^2) COMPLEXITY
# time = a * n^2 + b
# WHEN THERE ARE TWO LOOP THE ALGORITHMIC COMPLEXITY WILL BE 2 THAT MEANS N SQUARE

numbers = [ 3, 6, 2, 4, 3, 6, 8 , 9]

# FINDING DUPLICATES 
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i], " is a duplicate")
            break 


print("-----------Break-----------")
