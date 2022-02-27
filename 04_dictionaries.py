print("🧰🧰🧰 DICTIONARY 🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰")
# KEY / VALUE PAIR
# ASSOCIATIVE ARRAY, LIKE JAVA HASHMAP
# DICTS ARE UNORDERED
x = {'pork': 25.4, 'beef': 33.6, 'chicken': 22.51}
print(x) # {'pork': 25.4, 'beef': 33.6, 'chicken': 22.51}
x = dict([('pork', 25.3), ('beef', 33.6), ('chicken', 22.51)])
print(x) # {'pork': 25.3, 'beef': 33.6, 'chicken': 22.51}
x = dict(pork = 25.3, beef = 33.6, chicken = 22.51)
print(x) # {'pork': 25.3, 'beef': 33.6, 'chicken': 22.51}

print("🧰🧰🧰 DICTIONARY OPERATION 🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰")
x['shrimp']=38.2 # add or update
print(x) # {'pork': 25.3, 'beef': 33.6, 'chicken': 22.51, 'shrimp': 38.2}
del(x['shrimp']) # DELETE AN ITEM
print(x) # {'pork': 25.3, 'beef': 33.6, 'chicken': 22.51}
print(len(x)) # 3
x.clear() # DELETE ALL ITEMS
print(x) # {}
del(x)
# print(x) # NameError: name 'x' is not defined


print("🧰🧰🧰 ACCESSING KEYS AND VALUES 🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰")
# ACCESSING KEYS AND VALUES IN DICT (NOT COMPATIBLE WITH PYTHON 2)
y = {'pork': 25.4, 'beef': 33.6, 'chicken': 22.51}
print(y.keys()) # dict_keys(['pork', 'beef', 'chicken'])
print(y.values()) # dict_values([25.4, 33.6, 22.51])
print(y.items()) # dict_items([('pork', 25.4), ('beef', 33.6), ('chicken', 22.51)])
print("beef" in y) # True
print("meat" in y) # False
print(25.4 in y.values())  # True


print("🧰🧰🧰 ITERATING 🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰🧰")
# ITERATING A DICT - NOTE, ITEMS ARE IN RANDOM ORDER
for key in y:
    print(key, y[key])
    # pork 25.4
    # beef 33.6
    # chicken 22.51

for k,v in y.items():
    print(k, v)
    # pork 25.4
    # beef 33.6
    # chicken 22.51


























