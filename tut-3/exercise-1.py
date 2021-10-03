# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

expences = [2200, 2350, 2600, 2130, 2190]
# 1. In Feb, how many dollars you spent extra compare to January?
print(f'Extra expense in Feb is - {expences[1]-expences[0]}')
# 2. Find out your total expense in first quarter (first three months) of the year.
first_three_month = 0
for i in range(len(expences)):
    first_three_month += expences[i]
    if i == 2:
        print(f'First three month - {first_three_month}')
        break

# 3. Find out if you spent exactly 2000 dollars in any month
if 2000 in expences:
    print(True)
else:
    print(False)

try:
    print(expences.index(2000))
except ValueError as e:
    print(e)
    
    
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expences.append(1980)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your  # monthly expense list based on this
expences[3] = expences[3] - 200
print(expences)




