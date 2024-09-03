from typing import Any


# LinkedList
class Node:
    def __init__(self, val: Any):
        self.val: Any = val
        self.next: None | Node = None

    def __repr__(self) -> str:
        return f"<Node: {self.val}>"


class LinkedList:

    def __init__(self):
        self.head: Node | None = None

    def is_empty(self) -> bool:
        return self.head is None

    def search(self, element: Any) -> None | Node:
        curr: Node | None = self.head
        while curr:
            if curr.val == element:
                return curr
            curr = curr.next
        return None

    def add(self, element: Any) -> None:
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def size(self) -> int:
        curr: Node | None = self.head
        count: int = 0
        while curr:
            count += 1
            curr = curr.next

        return count

    def remove(self, element: Any):
        curr: Node | None = self.head
        prev: Node | None = None
        found: bool = False

        while curr and not found:
            if curr.val == element and self.head == curr:
                found = True
                self.head = curr.next
            if curr.val == element:
                found = True
                prev.next = curr.next
            else:
                prev = curr
                curr = curr.next

        return curr

    def insert(self, element: Any, index: int) -> None:
        if index == 0:
            self.add(element)
        if index > 0:
            new_node: Node = Node(element)
            curr: Node | None = self.head
            pos: int = index
            while pos > 1:
                curr = curr.next
                pos -= 1

            prev_node = curr
            next_node = curr.next

            prev_node.next = new_node
            new_node.next = next_node

    def __repr__(self) -> str:
        nodes = []

        curr: Node | None = self.head
        while curr:
            if curr is self.head:
                nodes.append(f"[Head: {curr.val}]")
            elif curr.next is None:
                nodes.append(f"[Tail: {curr.val}]")
            else:
                nodes.append(f"[{curr.val}]")
            curr = curr.next

        return " -> ".join(nodes)


l = LinkedList()
l.add(10)
l.add(40)
l.add(50)
l.add(60)
print("LinkedList: ", l)
print("Empty? ", l.is_empty())
print("Size: ", l.size())
print("Search: ", l.search(40))
l.insert(35, 2)
print("LinkedList: ", l)
print("Remove: ", l.remove(40))
print("LinkedList: ", l)
