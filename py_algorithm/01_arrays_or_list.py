# https://youtu.be/gDqQf4Ekr2A


# Store Apple's stock price for 5 days and answer

# 1. What was the price in day 3?
# 2. On what day price was 823?
# 3. Print all prices
# 4. Insert new price 613 at index 1
# 4. Delete element at index 1

def run():
    stock_prices = [239, 453, 145, 823, 345]

    """
    Internal memory representation (RAM):
        IDX     AOR      VAL
        ====================
        [0]   0x00500 -> 239
        [1]   0x00501 -> 453
        [2]   0x00508 -> 145
        [3]   0x0050A -> 823
        [4]   0x0050F -> 345
        
        IDX = Index
        AOR = Address on the RAM
        VAl = Value
        
        239 = 11101111 (Binary) 
        Here each single digit is a bit, for instance 1 is a bit
        Need 4 bytes to store the number, 4 bytes is the capacity of integer number in many programming languages
        1 byte is equal 8 bits (add zeros before to make 4 bytes)
        4 Bytes
        00000000  00000000  00000000  11101111 
        These 4 bytes are actually stored in the memory location
    """

    # ===== Answer to the question no 1 =====
    print(f"Price on day 3 is => {stock_prices[2]} and the memory address is => 0x00508")
    # Big-O = O(1) Constant time operation

    # ===== Answer to the question no 2 =====
    for i in range(len(stock_prices)):
        if stock_prices[i] == 823:
            return i
    # Big-O = O(n) Linear time complexity

    # ===== Answer to the question no 3 =====
    for price in range(len(stock_prices)):
        print(price)
    # Big-O = O(n) Linear time complexity

    # ===== Answer to the question no 4 =====
    stock_prices.insert(1, 613)  # It will shift all the items after indexed item to the next position
    # Big-O = O(n) Linear time complexity

    # ===== Answer to the question no 5 =====
    stock_prices.remove(4)  # Shift all elements to the upward
    # Big-O = O(n) Linear time complexity

    """
    
    Initial Allocation: When a dynamic array is first created, it allocates an initial block of memory. The size of this block is often a small number of elements (e.g., 4 or 8). 

    Insertion: When an element is inserted and there is still available capacity within the allocated block, the element is simply placed into the next available slot. This operation is very fast, 
    typically O(1) time complexity.When a dynamic array is first created, it allocates an initial block of memory. The size of this block is often a small number of elements (e.g., 4 or 8).
    
    Here’s a step-by-step example of inserting elements into a dynamic array:
    Initial Allocation: A dynamic array starts with an initial capacity of 4. It is currently empty.
        Array: [] (capacity: 4)
    Insertions: Insert elements 1, 2, 3, and 4.
        After inserting 1: [1]
        After inserting 2: [1, 2]
        After inserting 3: [1, 2, 3]
        After inserting 4: [1, 2, 3, 4] (Array is now full)
    Insertion with Resizing: Insert element 5. Since the array is full, it needs to resize.
        Allocate a new array with double the capacity (capacity: 8).
        Copy elements from the old array to the new array: [1, 2, 3, 4, _, _, _, _]
        Insert element 5: [1, 2, 3, 4, 5, _, _, _]
    """


if __name__ == "__main__":
    run()

# Problems and solution -> https://github.com/codebasics/data-structures-algorithms-python/blob/master
# /data_structures/2_Arrays/2_arrays_exercise.md
