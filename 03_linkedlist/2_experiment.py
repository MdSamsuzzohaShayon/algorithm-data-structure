# 0(1)
"""
Benefits
    1. Don't need to pre-allocate space
    2. Insertion is easier
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data)
    

    def print(self):
        itr = self.head
        llstr = ""
        while itr:
            suffix = ''
            if itr.next:
                suffix = "-->"
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)
    



if __name__ == "__main__":
    root = LinkedList()
    root.insert_at_end(255)
    root.insert_at_end(100)
    root.insert_at_end(50)
    root.print()
