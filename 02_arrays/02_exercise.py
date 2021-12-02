# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

monthly_expense = [2200, 2350, 2600, 2130, 2190]
print("1. Extra exponse in Feb - ",monthly_expense[1] - monthly_expense[0])

first_three_month = 0 
for i, val in enumerate(monthly_expense):
    if i == 3:
        break
    first_three_month += val

print("2. Total of first three month - ", first_three_month)


index = 0
match = False
while index < len(monthly_expense):
    if monthly_expense[index] == 2000:
        match = True 
        break 
    index = index+ 1

print(f"3. Found 2000 in the list? {match}")


monthly_expense.append(1980)
print("4. appended for month of may - ", monthly_expense)



monthly_expense[3] = monthly_expense[3] + 200
print("5. After getting refund in month of april - ", monthly_expense[3])
