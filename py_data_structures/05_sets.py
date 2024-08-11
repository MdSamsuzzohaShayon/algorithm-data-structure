from typing import Set

# Link to a tutorial about Python data structures
# Tutorial-1: https://youtu.be/qv41OR37Syo
# Official Python documentation on sets
# Docs: https://docs.python.org/3/tutorial/datastructures.html#sets

"""
Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating 
duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
"""

# Define a set with some duplicate elements
utensils: Set[str] = {"fork", "spoon", "knife", "knife", "knife"}  # Sets automatically remove duplicates
# Output: {'fork', 'spoon', 'knife'}

# Add an element to the set
utensils.add("napkin")  # Adds 'napkin' to the set
# Output: {'fork', 'spoon', 'knife', 'napkin'}

# Remove specific elements from the set
utensils.remove("fork")  # Removes 'fork' from the set
utensils.remove("spoon")  # Removes 'spoon' from the set
# Output: {'knife', 'napkin'}

# Define another set
dishes: Set[str] = {"Bowl", "Plate", "Cup", "knife"}  # 'knife' is also in this set
# Output: {'Bowl', 'Plate', 'Cup', 'knife'}

# Update the 'utensils' set with elements from 'dishes' (commented out in the code)
# utensils.update(dishes)  # This would add elements from 'dishes' to 'utensils'

# Iterate over elements in the 'utensils' set
for x in utensils:
    print(x)  # Prints each element in 'utensils'

# Perform set operations
dinner_table: Set[str] = utensils.union(dishes)  # Union of 'utensils' and 'dishes'
print("Join: ", dinner_table)  # Output: {'Bowl', 'Plate', 'Cup', 'knife', 'napkin'}

difference: Set[str] = dishes.difference(utensils)  # Elements in 'dishes' but not in 'utensils'
print("Difference: ", difference)  # Output: {'Cup', 'Bowl', 'Plate'}

intersection: Set[str] = dishes.intersection(utensils)  # Elements common to both 'dishes' and 'utensils'
print("Common: ", intersection)  # Output: {'knife'}

# Time and Space Complexity:
# Adding an element to a set: O(1) on average. Sets use hash tables, making insertion and lookup operations fast.
# Removing an element from a set: O(1) on average.
# Set operations (union, difference, intersection): O(n) where n is the number of elements in the sets involved.
# Iterating over a set: O(n) where n is the number of elements in the set.
# Space Complexity: O(n) where n is the number of elements in the set. Sets store elements in a hash table, which requires linear space relative to the number of elements.


# Make comments and explain everything in the comments. Add more explanation here in the form of comments in terms of data structure. Determine time and space complexity (in comments).
# And use static typing properly
