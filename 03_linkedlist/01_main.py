# 0(1) 
"""
Benefits 
    1. Don't need to pre-allocate space
    2. Insertion is easier
"""


class Node:
    def __init__(self, data= None, next=None):
        self.data =data
        self.next =next


class LinkedList: 
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        print("Node - ", node)
        self.head = node 

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            
        itr = self.head
        count = 0
        while itr:
            if count  == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
            
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1
            
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
            

    def print(self):
        itr = self.head 
        llstr = ""
        while itr:
            suffix = ''
            if itr.next:
                suffix = "-->"
            print("Itr - ", itr)
            print("Itr data - ", itr.data)
            llstr += str(itr.data) + suffix
            print("Itr next - ", itr.next)
            itr = itr.next
        print(llstr)
    
    def get_length(self):
        count = 0 
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count



if __name__ == "__main__":
    root = LinkedList() 
    # root.insert_at_beginning(5)
    # root.insert_at_beginning(10)
    # root.insert_at_beginning(15)
    root.insert_at_end(255)
    root.insert_at_end(123)
    root.insert_at_end(452)
    root.insert_at(1, 40)
    root.print()
    root.remove_at(2)
    root.print()
    root.insert_values(["Banana", "mangoose"])
    root.print()
    print(root.get_length())