"""
YouTube Tutorial: https://www.youtube.com/watch?v=-gjxg6Pln50
The Two Pointers technique is a popular approach in algorithmic problem-solving where two pointers
iterate through the data structure in tandem. It's often used to optimize solutions for problems
involving arrays or linked lists. Python makes it easy to implement the Two Pointers technique
due to its simple syntax and array-handling capabilities.
"""


def two_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [nums[left], nums[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

# Example usage:
sorted_array = [-2, 1, 2, 4, 7, 11]
target_sum = 13
result = two_sum(sorted_array, target_sum)

if result:
    print(f"Pair with sum {target_sum}: {result}")
else:
    print("No pair found.")


"""
In this example, left and right are the two pointers initialized at the beginning and end of the 
sorted array. The pointers move towards each other until they meet or find the target sum.

The Two Pointers technique is particularly useful for optimizing the time complexity 
of certain problems by avoiding unnecessary computations.
"""