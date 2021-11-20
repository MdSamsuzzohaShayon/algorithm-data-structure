# Time 1:10:00

# LOOKING FOR THE POSITION IN THE LIST WHERE THE VALUE EXIST 
def linear_search(list, target):
    # RETURN INDEX POSITION IF FOUND ELSE RETURN NONE 
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print(f'target found at index: {index}')
    else: 
        print("target not found")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(numbers, 12)
verify(result)  # EXPECTED RESULT - target not found


result = linear_search(numbers, 6)
verify(result)  # EXPECTED RESULT - target found at index: 5

"""
1. THIS ALGORITHM RETURNED A RESULT IN EACH CASE 
2. IT EXECUTED IN A FINITE TIME 
3. RESULT WAS EXPECTED 
"""