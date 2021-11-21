#  Time - 1:28:00

# THIS WILL RETURN TRUE INSTEAD OF INDEX NUMBER IF IT EXIST 
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False 
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else: 
            if list[midpoint] < target:
                # LIST STARTING FROM MIDDLE AND GETTING REST OF THE ELEMENT IN NEW LIST 
                middle_to_end = list[midpoint+1:]
                return recursive_binary_search(middle_to_end, target)
            else:
                middle_to_start = list[:midpoint]
                return recursive_binary_search(middle_to_start, target)

def verify(result):
    print("Target found - ", result)



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(numbers, 12)
verify(result)  # EXPECTED RESULT - target not found


result = recursive_binary_search(numbers, 6)
verify(result)  # EXPECTED RESULT - target found at index: 5

"""
A RECURSIVE FUNCTION IS ONE THAT CALL ITSELF

"""