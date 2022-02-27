# ENQUEUE - ADD AN ITEM TO THE END OF THE LINE
# DEQUEUE - REMOVE AN ITEM FROM THE BEGINNING OG THE LINE
# FIFO - FIRST-IN-FIRST-OUT

print("🔩🔩🔩 QUEUE 🔸🔹▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹▪️ ▫🔹▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫")
# QUEUES ARE GOOD FOR MODELING ANYTHING YOU WAIT IN LINE FOR
# ANK TELLERS, PLACING AN ORDER AT MCDONALD
# DMV CUSTOMER SERVICE. SUPERMARKET CHECKOUT

from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue) # deque([5, 10])
print(my_queue.popleft()) # deque([5, 10])


# 54:46
# MAXHEAP - COMPLETE BINARY TREE
# EVERY NODE <= ITS PARENT
# IT IS FAST
# INSERT IN O(log n)
# GET MAX IN O(1)
# REMOVE MAX IN O(log n)
# EASY TO IMPLEMENT
# USING A LIST