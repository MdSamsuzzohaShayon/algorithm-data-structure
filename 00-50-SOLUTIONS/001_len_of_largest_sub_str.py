"""
Given a string, find the length of the longest substring without repeating characters.
Examples:
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

# Iteration through the string
def len_of_longest_substring(s) -> int:
    """
    :type s: str
    :rtype: int
    """
    mapSet = {}
    start, result = 0, 0

    for i in range(len(s)):
        # Checking for repeating characters. if this element is found in the sets, get the value of that element and
        # compare with start If the current character s[i] is already in mapSet (indicating it's a repeating
        # character), update the start index to the maximum of its current value and the index stored in mapSet[s[
        # i]]. This ensures that the starting point of the substring moves to the next index after the last
        # occurrence of the repeating character.
        if s[i] in mapSet:
            start = max(mapSet[s[i]], start)
        # Calculate the length of the current substring without repeating characters (i - start + 1)
        # and update result to store the maximum length encountered so far.
        result = max(result, i - start + 1) # Get the highest value from the result and index after reducing start
        # Updating the index in mapSet: Store the index of the current character s[i] in mapSet for future reference.
        mapSet[s[i]] = i + 1 # Assign value to set

    # Returning the final result: Returns the length of the longest substring without repeating characters.
    return result


print(len_of_longest_substring('abcabcbb'))  # Expected 3
# print(len_of_longest_substring('bbbbb'))  # Expected 1
# print(len_of_longest_substring('pwwkew'))  # Expected 3
