from typing import List
import itertools

"""
Tutorial-1: https://youtu.be/VA7OBaTUGNY
Tutorial-2: https://youtu.be/j5fnaXLOkFk
Tutorial-3: https://youtu.be/UdZ4yxf-F4M
"""


# ====================================
# CARTESIAN PRODUCT IN PYTHON
# ====================================

# Function to calculate Cartesian product
def cartesian_product(*sets):
    """
    This function takes any number of sets as input and returns the Cartesian product
    as a list of tuples, where each tuple is a combination of one element from each set.
    """
    if not sets:
        return [()]  # Return an empty tuple if no sets are provided
    result = [[]]
    for set_ in sets:
        result = [x + [y] for x in result for y in set_]
    return [tuple(x) for x in result]


"""
The Cartesian Product is a fundamental operation in mathematics and computer science that returns 
all possible ordered pairs (or tuples in general) from two or more sets.

Mathematical Definition:
    If A and B are two sets, then the Cartesian product A x B is the set of all ordered pairs (a, b)
    where 'a' belongs to set A and 'b' belongs to set B.

Properties:
    - Order Matters: (a, b) is not the same as (b, a).
    - Size: If set A has m elements and set B has n elements, then A x B will have m * n elements.
"""

# ====================================
# EXAMPLE 1: Coffee Shop Menu Combinations
# ====================================

"""
Imagine a coffee shop where customers can choose from a list of coffee types, flavors, and milk options.
The Cartesian product of these lists will give all possible combinations of coffee, flavor, and milk.

Sets:
    - Coffee: ['Cappuccino', 'Latte', 'Americano']
    - Flavor: ['Vanilla', 'Hazelnut', 'Mocha']
    - Milk: ['Skim', '2%', 'None']

Cartesian Product:
    - The result will be all possible combinations of these three sets.
"""

coffee: List[str] = ["Cappuccino", "Latte", "Americano"]
flavor: List[str] = ["Vanilla", "Hazelnut", "Mocha"]
milk: List[str] = ["Skim", "2%", "None"]

print("All Coffee Combinations:")
for combination in itertools.product(coffee, flavor, milk):
    print(combination)

# ====================================
# EXAMPLE 2: Clothing Combinations
# ====================================

"""
Consider a scenario where a person can choose from a list of shirts and pants. The Cartesian product
will give all possible clothing combinations.

Sets:
    - Shirts: ['Red', 'Blue', 'Green']
    - Pants: ['Jeans', 'Shorts']

Cartesian Product:
    - The result will be all possible combinations of shirts and pants.
"""

shirts: List[str] = ["Red", "Blue", "Green"]
pants: List[str] = ["Jeans", "Shorts"]

print("\nAll Clothing Combinations:")
for combination in itertools.product(shirts, pants):
    print(combination)

# ====================================
# EXAMPLE 3: Cartesian Product of Numeric Sets
# ====================================

"""
The Cartesian product can also be applied to numerical sets, generating all possible pairs of numbers.

Sets:
    - A: [1, 2]
    - B: [3, 4, 5]

Cartesian Product:
    - The result will be all possible pairs (a, b) where 'a' is from A and 'b' is from B.
"""

A: List[int] = [1, 2]
B: List[int] = [3, 4, 5]

print("\nCartesian Product of Numeric Sets:")
for combination in itertools.product(A, B):
    print(combination)

# ====================================
# EXAMPLE 4: Product Configurations
# ====================================

"""
Imagine an e-commerce platform that offers products with various configurations, such as color, size, 
and material. The Cartesian product will generate all possible configurations.

Sets:
    - Colors: ['Red', 'Blue', 'Black']
    - Sizes: ['Small', 'Medium', 'Large']
    - Materials: ['Cotton', 'Polyester', 'Wool']

Cartesian Product:
    - The result will be all possible combinations of color, size, and material.
"""

colors: List[str] = ["Red", "Blue", "Black"]
sizes: List[str] = ["Small", "Medium", "Large"]
materials: List[str] = ["Cotton", "Polyester", "Wool"]

print("\nAll Product Configurations (without itertools):")
for combination in cartesian_product(colors, sizes, materials):
    print(combination)
# ====================================
# EXAMPLE 5: Multi-Dimensional Data in Databases
# ====================================

"""
In databases, Cartesian products can be used to generate all possible combinations of attributes 
for data analysis or search queries.

Consider a database that stores product attributes:
    - Category: ['Electronics', 'Furniture']
    - Brand: ['BrandA', 'BrandB']
    - Warranty: ['1 year', '2 years']

Cartesian Product:
    - The result will be all possible combinations of category, brand, and warranty.
"""

categories: List[str] = ["Electronics", "Furniture"]
brands: List[str] = ["BrandA", "BrandB"]
warranties: List[str] = ["1 year", "2 years"]

print("\nAll Product Attribute Combinations (without itertools):")
for combination in cartesian_product(categories, brands, warranties):
    print(combination)

# ====================================
# PERFORMANCE CONSIDERATION
# ====================================

"""
Time Complexity:
    - The time complexity of calculating the Cartesian product is determined by the number of combinations generated.
    - General Case (Using Custom Function):
        - Let's say you have n sets, and each set S_i contains m_i elements.
        - The total number of combinations (tuples) generated by the Cartesian product will be:
          T = m_1 * m_2 * ... * m_n
        - The time complexity to generate all these combinations will be O(T) because you need to iterate over each combination and add it to the result.
    - Worst Case:
        - If each set contains m elements and there are n sets, the time complexity will be O(m^n).
        - This represents an exponential time complexity, which can grow very large when n increases.

Space Complexity:
    - The space complexity depends on the storage needed for the result.
    - General Case (Using Custom Function):
        - The space complexity is also O(T), where T is the total number of combinations (tuples) generated.
        - Additionally, the space used by the intermediate lists during the construction of each combination must be considered. However, the primary factor is the space required to store the final list of combinations.
    - Worst Case:
        - If each combination is stored as a tuple, and there are T such tuples, the space complexity becomes O(T * n), where n is the length of each tuple.

Performance Considerations:
    - Combinatorial Explosion:
        - The Cartesian product grows exponentially as the number of sets (n) or the size of the sets (m) increases. This can lead to a significant performance bottleneck in both time and space.
        - Example: If you have 5 sets with 10 elements each, the total combinations will be 10^5 = 100,000, leading to a time complexity of O(100,000) and space complexity of O(100,000 * 5).
"""

# ====================================
# SUMMARY
# ====================================

"""
The Cartesian product is a versatile tool in both mathematics and programming, especially in scenarios 
involving combinations, multi-dimensional data, and configuration generation. In Python, the `itertools.product`
function is an efficient way to compute the Cartesian product of multiple sets or lists. However, understanding 
the underlying principles and potential performance implications is crucial, especially when dealing with large datasets.
"""
