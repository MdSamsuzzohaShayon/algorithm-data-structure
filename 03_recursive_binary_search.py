#  Time - 1:28:00

"""
A recursive function is one that calls itself
Recursive function must need a terminating condition
Iterative solution - the solution implement using loop structure
Recursive solution - A set of stopping condition and a function that it calls itself
Python as a maximum recursion depth afterward it will halt, however, python prefer iterative solution

"""

# THIS WILL RETURN TRUE INSTEAD OF INDEX NUMBER IF IT EXIST IT WILL RETURN TRUE OR FALSE VALUE
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
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                # THIS FUNCTION HAS LIST OF MIDDLE TO START - SO IT'S SPILLITING THE LIST AND CREATING A NEW LIST 
                return recursive_binary_search(list[:midpoint], target)

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