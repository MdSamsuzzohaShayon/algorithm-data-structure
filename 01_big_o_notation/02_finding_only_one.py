# 0(1) - TIME WILL BE CONSTANT DOESN'T MATTER HOW MANY ITEM 
# IN AN LIST BECAUSE WE ARE SUPPOSE TO GET ONLY ONE ITEM 
# FROM THE ARRAY

def find_first_pe(prices, eps, index):
    pe = prices[index] / eps[index]
    return pe 

prices = [50, 55, 60, 66]
eps = [10, 15, 20, 26]
val = find_first_pe(prices, eps, 2)
print(val)