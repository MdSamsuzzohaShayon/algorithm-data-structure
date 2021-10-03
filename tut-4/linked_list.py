class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beganning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        # IF LINKED LIST IS BLANK
        if self.head is None:
            self.head = Node(data, None)  # HERE NODE JS NEXT
            return
        
        # IF LINKED LIST IS NOT VACANT OR BLANK
        # ITERATE TO LINK LIST AND TO AT THE END -> AND INSERT
        itr = self.head
        # IF ITERATE DOT NEX HAS SOME VALUE THAT MEAN IT'S NOT THE END
        while itr.next:
            itr = itr.next
            
        # IF ITERATE DOR NEXT ELEMENT BECOME NULL THAT MEAN WE ARE ON LAST ELEMENT
        itr.next = Node(data, None)
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr=itr.next
        return count
    
    def remove_at(self, index):
        # VALIDATE INDEX
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        # WHAT IF WE TRY TO REMOVE HEAD
        if index == 0:
            # POINTING TO NEXT ELEMENT
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
                
            itr = itr.next
            count += 1
            
    
        
        
    
    def print(self):
        if self.head is None:
            print("Linked list is vacant")
            
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' ---> '
            itr = itr.next
        
        print(llstr)


if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_beganning(5)
    # ll.insert_at_beganning(89)
    # ll.insert_at_end(59)
    # ll.insert_at_end(12)
    # ll.insert_at_end(12283)
    print("length - ", ll.get_length())
    ll.insert_values(["banana", "mango", "nodejs", "reactjs"])
    ll.remove_at(2)
    # ll.remove_at(20) #EXCEPTION
    ll.print()
    
    
    
