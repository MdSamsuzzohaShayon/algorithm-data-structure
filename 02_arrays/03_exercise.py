heros=['spider man','thor','hulk','iron man','captain america']
print("1. Length - ", len(heros))

heros.append("Black Panther")
print("2. Black pater at the end - ", heros)

heros.remove("Black Panther")
heros.insert(3, "Black Panther")
print("3. After hulk - ", heros)

heros[1:3]=['doctor strange']
print(heros)
# 5. Sort the list in alphabetical order
heros.sort()
print(heros)