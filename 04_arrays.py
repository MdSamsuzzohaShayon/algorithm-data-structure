# Time - 2:09:00

# THE VALUES OF LIST ARE STORED IN MEMORY 
# THE ARRAYS STORES REFERENCES TO EACH OF THOSE OBJECTS 
# TO ACCESS A VALUE NEED TO USE A SUBSCRIPT ALONG WITH AN INDEX VALUE 
new_list = [1, 2, 3]
result = new_list[0]
print(result)


# THE IN OPERATOR ACTUALLY CALLS A CONTAINS METHOD THAT IS DEFINED ON THE LIST TYPE WHICH RUNS A LINEAR SEARCH OPERATION
if 1 in new_list:
    print(True)

# LINEAR SEARCH 
for n in new_list:
    if n == 1:
        print(True)
        break

# IF ARRAY WERE SORTED WE COULD USE BINARY SEARCH 
# BECAUSE SORT OPERATIONS INCUR A COST OF THEIR OWN LANGUAGES USUALLY STAY AWAY FROM SORTING THE LIST


"""MOST ARRAY SUPPORT THREE TYPES OF INSERT OPERATIONS 1. TRUE INSERT - USING AN INDEX VALUE INSERT ANYWHERE IN THE LIST (THIS OPERATION HAS A LINEAR RUNTIME) WHEN WE INSERT AT THE START OF THE 
LIST THE ITEM IS CURRENTLY IN THAT SPOT MOVE TO THE NEXT SPOT, SECOND ITEM MOVE TO THE NEXT POSITION THIS KEEPS HAPPENING UNTIL ALL ELEMENT HAVE BEEN SHIFTED FORWARD ONE INDEX POSITION. SO IN THIS 
WORSE CASE SCENARIO. WE KNOW, ANY OPERATION THAT INVOLVES ITERATING THROUGH EVERY SINGLE VALUE MEANS A LINEAR RUNTIME. 2. APPEND ITEM - APPENDING ALTHOUGH TECHNICALLY AN INSERT OPERATION IN THAT IS 
INSERTS AN ITEM INTO AN EXISTING ARRAY DOESN'T INCUR THE SAME RUNTIME COST BECAUSE APPENDS SIMPLY ADD THE ITEM TO THE END OF THE LIST"""

"""
LIST RESIZE OPERATION - PYTHON DOES NOT RESIZE THE LIST TO ACCOMMODATE JUST THE ELEMENT WE WANT TO ADD
INSTEAD IT WOULD ALLOCATE 4 BLOCKS OF MEMORY TO INCREASE THE SIZE TO A TOTAL OF 4 CONTIGUOUS BLOCKS OF MEMORY
IT DOES THIS SO THAT IT DOESN'T HAVE TO RESIZE THE LIST EVERY SINGLE TIME WE ADD A ELEMENT BUT AT VERY SPECIFICS POINTS.
THE GROWTH PATTERN OF THE LIST TYPE IN PYTHON IS 0, 4, 8, 16, 25, 35, 46 AND SO ON
"""


# EXTENDS TAKES ANOTHER LIST TO ADD, 
# EXTEND EFFECTIVELY MAKES A SERIES OF APPEND CALLS ON EACH OF THE ELEMENTS IN THE NEW LIST UNTIL ALL OF THEM HAVE BEEN APPENDED TO THE ORIGINAL LIST
# THIS OPERATION HAS A RUNTIME OF BIG O OF K 
# K REPRESENTS THE NUMBER OF ELEMENTS IN THE LIST THAT WE ARE ADDING TO OUR EXISTING LIST
numbers = []
numbers.extends([3,4,5])


# DELETE OPERATION - DELETE IS SIMILAR TO INSERT IN THAT WHEN DELETE OPERATION OCCURS THE LIST NEEDS TO MAINTAIN CORRECT INDEX VALUES 
# SO WHERE AN INSERT SHIFTS EVERY EVERY ELEMENT TO THE RIGHT A DELETE OPERATION SHIFTS EVERY ELEMENT TO THE LEFT
# DELETE OPERATION HAVE AN UPPER BOUND OF BIG O OF N = O(n) LINEAR RUNTIME





