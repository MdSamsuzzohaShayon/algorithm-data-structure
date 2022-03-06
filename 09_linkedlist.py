# https://www.youtube.com/watch?v=kQDxmjfkIKY&t=87s - 1:08:31
# LET'S SAY WE HAVE COLLECTION OF ITEMS TO BE STORED
# AND WE WANT TO ITERATE THOUGH THEM SO WE CAN FIND AN ITEM IN THE LIST
# WOULDN'T BE ABLE TO INSERT AN ITEM BUT NEED VERY FAST SEARCHING SPEED SPECIALLY AT THE FRONT OF THE LIST
# ABLE TO REMOVE ITEM FROM THE LIST
# ITERATE FORWARD AND BACKWARD THOUGH THE LIST OR POSSIBLY EVENT IN A CONTINUOUS CIRCLE THOUGH THE LIST
# ONE POSSIBLE STORAGE SOLUTION IS LINKED LIST

# EVERY LINKEDLIST WLL BE COMPOSED OF NODE THERE WE CAN STORE ANY KIND OF DATA
# EACH NODE CONNECTED TO NEXT NODE SO IT HAS A POINTER
# IN THE LAST NODE THERE WILL BE NO NEXT POINTER
# FIRST NODE IS CALLED ROOT NODE

# ATTRIBUTES - ROOT: POINTER TO THE BEGINNING OF THE LIST, SIZE: NUMBERS OF THE NODES IN LIST
# OPERATIONS - FIND(DATA), ADD(DATA), REMOVE(DATA), PRINT_LIST()

# NODE CLASS HAS A CONSTRUCTOR THAT SETS THE DATA PASSED IN AND OPTIONALLY AND PREVIOUS NODE
# IF ALSO HAS A STR METHOD TO GIVE A STRING REPRESENTATION FOR PRINTING
# NODE THAT PREV_NODE IS ONLY USED IN DOUBLY LINKED LIST

class Node:

    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return '(' + str(self.data) + ')'


# A LINKED LIST OBJECT HAS TWO ATTRIBUTES: A ROOT NODE THAT DEFAULTS TO NODE - ADD, FIND, REMOVE, PRINT_LIST
print("\n\n🔩🔩🔩 REGULAR LINKEDLIST 🔸🔹▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹▪️ ▫🔹▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫")
class LinkedList:

    def __init__(self , r=None):
        self.root = r
        self.size = 0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node =this_node
                this_node = this_node.next_node
        return False

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end = '->')
            this_node = this_node.next_node
        print(None)

my_list = LinkedList()
my_list.add(5)
my_list.add(8)
my_list.add(12)
my_list.print_list()

print("Size = " + str(my_list.size))
my_list.remove(8)
print("Size = " + str(my_list.size))
print(my_list.find(5))
print(my_list.root)



print("\n\n🔩🔩🔩 CIRCULAR LINKEDLIST 🔸🔹▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹▪️ ▫🔹▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫")
class CircularLinkedList: # LOOP BACK TO ROOT IN CIRCULAR LINKEDLIST

    def __init__(self , r=None):
        self.root = r
        self.size = 0

    def add(self, d): # CHANGE FOR CIRCULAR
        if self.size == 0:
            self.root = Node(d)
            self.root.next_node = self.root
        else:
            new_node = Node(d, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while True:
            if this_node.data == d: # FOUND
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True # DATA REMOVED
            elif this_node.next_node == self.root:
                return False # DATA NOT FOUND
            prev_node = this_node
            this_node = this_node.next_node

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end="->")
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node, end='->')
        print()

cll = CircularLinkedList()
for i in [5,6,7,3,4,8]:
    cll.add(i)

print("Size = " + str(cll.size))
print(cll.find(3))
print(cll.find(12))
my_node = cll.root
print(my_node, end="->")
for i in range(8):
    my_node = my_node.next_node
    print(my_node, end="->")
print()