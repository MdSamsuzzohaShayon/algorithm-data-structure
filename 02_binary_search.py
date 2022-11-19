# Time - 1:18:00

def binary_search(list, target):
    first = 0 # track the position of the array
    last = len(list) - 1 # last involves a call to the len function, this is a constant time operation

    """    
    WHILE LOOP IS WHAT CAUSES THE RUNTIME TO GROW 
    EVEN THOUGH ALL WE ARE DOING IS A COMPARISON OPERATION - RUN AS MANY TIMES AS IT NEEDS UNTIL A FIRST IS EQUAL OR GRATER THAN LAST 
    EACH TIME THE LOOP DOES THIS THE SIZE OF THE DATA SET THE SIZE OF THE LIST GROWS SMALLER BY CERTAIN FACTOR UNTIL IT APROCHES A SINGLE ELEMENT
    WHICH IS WHAT RESULT IN LOGARITHMIC RUNTIME
    """
    while first <= last:
        # CALCULATE MIDPOINT OF THE LIST
        # HERE // MEANS FLOOR DIVISION OPERATOR
        midpoint = (first + last) // 2  # Runtime for simple division is constant

        if list[midpoint] == target: # reading a video from the list and target both of them are constant time operation
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last  = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print(f'target found at index: {index}')
    else: 
        print("target not found")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(numbers, 12)
verify(result)  # EXPECTED RESULT - target not found


result = binary_search(numbers, 6)
verify(result)  # EXPECTED RESULT - target found at index: 5


"""
THE NUMBERS LIST THAT WE'VE DEFINED HAS TO BE SORTED
BINARY SEARCH RELIES ON THE FACT THAT IF THE TARGET IS GRATER THAN THE MIDPOINT THEN OUR POTENTIAL VALUE LIE TOT HE LEFT
SINCE THE VALUES ARE SORTED IN ASCENDING ORDER
IF THE VALUES ARE UNSORTED OUR IMPLEMENTATION OF BINARY SEARCH MAY RETURN NONE EVEN IF THE VALUE EXIST
"""