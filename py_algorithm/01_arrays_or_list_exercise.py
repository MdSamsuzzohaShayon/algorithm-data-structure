# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

"""
Let us say your expense for every month are listed below,
    January - 2200
    February - 2350
    March - 2600
    April - 2130
    May - 2190

Create a list to store these monthly expenses and using that find out


1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
"""

print("Exercise 1: =======================================================================================")
monthly_expenses = [2200, 2350, 2600, 2130, 2190]

print("1. Extra cost in Feb ", monthly_expenses[1] - monthly_expenses[0])

print("2. Total expense in first quarter: ", monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2])

# item_to_find = 2000
# found_items = [item for item in monthly_expenses if item == item_to_find]
# print("3. Found item " if found_items else "3. Not found ")

print("3. Did I spent 2000$ in any month? ", 2000 in monthly_expenses)

monthly_expenses.append(1980)
print("4. Add 1980 to monthly expenses", monthly_expenses)

# money_lost_april = monthly_expenses[3] - 300
# monthly_expenses[3] = money_lost_april
# print("5. Refund on return ", monthly_expenses)
monthly_expenses[3] = monthly_expenses[3] - 300
print("5. Refund on return ", monthly_expenses)

print("Exercise 2: =======================================================================================")
"""
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

"""
heros=['spider man','thor','hulk','iron man','captain america']
print("1. Length: ", len(heros))
heros.append("black panther")
print("2. add 'black panther'", heros)
heros.pop()
heros.insert(3, "black panther")
print("3. add 'black panther' after 'hulk'", heros)

# heros.remove('thor')
# heros.remove('hulk')
# heros.insert(1, "Doctor Strange")
# print("4. replace thor and hulk with doctor strange", heros)


heros[1:3] =["Doctor Strange"]
print("4. replace thor and hulk with doctor strange", heros)

heros.sort()
# print(dir(heros))
print("5. Sort the heros: ", heros)


print("Exercise 3: =======================================================================================")
max_num = int(input("Enter max number: "))
odd = []
for n in range(1, max_num):
    odd.append(n) if n % 2 != 0 else None

print("Odd: ", odd)
