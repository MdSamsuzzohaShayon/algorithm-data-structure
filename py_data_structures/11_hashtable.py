from typing import Any, List, Tuple, Optional

"""
Tutorial-1: https://youtu.be/ea8BRGxGmlA
Tutorial-2: https://youtu.be/54iv1si4YCM
"""


class HashTable:
    def __init__(self, MAX: int = 100) -> None:
        """
        Initialize a HashTable with a fixed size (100).
        Each slot in the array will contain a list to handle collisions (chaining method).
        """
        self._MAX: int = MAX  # Size of the hash table
        self._arr: List[List[Tuple[str, Any]]] = [[] for _ in range(self._MAX)]  # Array of empty lists to handle collisions

    def get_hash(self, key: str) -> int:
        """
        Hash function to calculate the index for a given key.

        Args:
            key (str): The key to be hashed.

        Returns:
            int: The computed hash index (0 <= hash < 100).

        Time Complexity: O(K) where K is the length of the key.
        """
        h: int = 0
        for char in key:
            h += ord(char)  # Calculate ASCII value of each character and sum them
        return h % self._MAX  # Return the modulo of the sum to stay within the bounds of the array size

    def add(self, key: str, val: Any) -> None:
        """
        Add a key-value pair to the hash table. If the key already exists, append the new value as a tuple.

        Args:
            key (str): The key to be added/updated.
            val (Any): The value associated with the key.

        Time Complexity: O(N) where N is the number of items in the list at the computed index.
        In the average case, this is O(1) because the number of items per list is small.
        """
        h = self.get_hash(key)
        # Check if the key already exists
        found = False
        for i, element in enumerate(self._arr[h]):
            if len(element) == 2 and element[0] == key:
                # If key is found, append the new value to the list of values
                self._arr[h].append((key, val))  # Append the new tuple
                found = True
                break
        if not found:
            # If the key does not exist, append a new tuple
            self._arr[h].append((key, val))

    def __setitem__(self, key: str, val: Any) -> None:
        """
        Magic method to allow setting a value using the index notation.
        Supports adding multiple values with the same key as tuples.

        Args:
            key (str): The key to be set.
            val (Any): The value associated with the key.

        Time Complexity: O(N), see add method for explanation.
        """
        self.add(key, val)

    def get(self, key: str) -> Optional[List[Tuple[str, Any]]]:
        """
        Retrieve all values associated with a given key.

        Args:
            key (str): The key whose values are to be retrieved.

        Returns:
            Optional[List[Tuple[str, Any]]]: A list of tuples (key, value) associated with the key, or None if the key is not found.

        Time Complexity: O(N) where N is the number of items in the list at the computed index.
        In the average case, this is O(1).
        """
        h = self.get_hash(key)
        values = [element for element in self._arr[h] if element[0] == key]
        return values if values else None  # Return list of tuples or None if no values are found

    def __getitem__(self, key: str) -> Optional[List[Tuple[str, Any]]]:
        """
        Magic method to allow getting values using the index notation.

        Args:
            key (str): The key whose values are to be retrieved.

        Returns:
            Optional[List[Tuple[str, Any]]]: A list of tuples (key, value) associated with the key, or None if the key is not found.

        Time Complexity: O(N), see get method for explanation.
        """
        return self.get(key)

    def __delitem__(self, key: str) -> None:
        """
        Magic method to delete all key-value pairs associated with the given key.

        Args:
            key (str): The key to be deleted.

        Time Complexity: O(N) where N is the number of items in the list at the computed index.
        In the average case, this is O(1).
        """
        h = self.get_hash(key)
        self._arr[h] = [element for element in self._arr[h] if element[0] != key]  # Remove all tuples with the given key

    @property
    def arr(self) -> List[List[Tuple[str, Any]]]:
        """
        Property to access the internal array of the hash table.

        Returns:
            List[List[Tuple[str, Any]]]: The internal array of lists (hash table with chaining).

        Time Complexity: O(1) (constant time).
        """
        return self._arr


# Example usage of the HashTable
t = HashTable()
print(t.get_hash("March 6"))  # Example: prints hash for "March 6"
t.add("Jan 12", 300)
t.add("Feb 13", 400)
t.add("Mar 14", 700)
t.add("Apr 15", 200)
t["Mar 6"] = 900
t["Mar 6"] = 1900
print(t.arr)
print("Prices in Mar:", t["Mar 6"])  # Should print: [('Mar 6', 900), ('Mar 6', 1900)]
print("Prices in Apr:", t.get("Apr 15"))  # Should print: [('Apr 15', 200)]
t["May 17"] = 500
print("Prices in May:", t["May 17"])  # Should print: [('May 17', 500)]
del t["Mar 14"]
print("Deleted Mar 14:", t.get("Mar 14"))  # This should print 'None' since the key was deleted
