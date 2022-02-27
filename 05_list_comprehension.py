print("🔩🔩🔩 LIST COMPREHENSION 🔸🔹▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹▪️ ▫🔹▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫")
# BASIC FORMAT: NET_LIST = [TRANSFORM SEQUENCE [ FILTER]]
import random
under_10 = [x for x in range(10)]
print("Under 10: " + str(under_10)) # Under 10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [x**2 for x in under_10]
print("Squares: ",  squares) # Squares:  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

odds = [x for x in under_10 if x % 2 == 1] # GET ODDS NUMBER
print("ODDS: ", str(odds)) # ODDS:  [1, 3, 5, 7, 9]

ten_x = [x* 10 for x in under_10 ]
print("Ten x: ", str(ten_x)) # Ten x:  [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

s = 'I love 2 go t0 the store 7 time a w3ek'
nums = [x for x in s if x.isnumeric()] # GET ALL NUMBERS FROM STRING
print("Nums: " + ''.join(nums)) # Nums: 2073

names = ['Cristiano', "Mbappe", "Luka", "Benzama"]
idx = [k for k,v in enumerate(names) if v == "Luka"]
print("Index - " + str(idx[0])) # Index - 2

letters = [x for x in "ABCDEF"]
random.shuffle(letters)
letrs = [a for a in letters if a != 'C']
print(letters, letrs) # ['F', 'B', 'D', 'C', 'A', 'E'] ['F', 'B', 'D', 'A', 'E']

# NESTED LOOP ITERATION FOR 2D LIST
# B IS THE SUBSETS , X IS THE VALUES
a = [[1,2], [3,4]]
new_list = [x for b in a for x in b]
print(new_list) # [1, 2, 3, 4]