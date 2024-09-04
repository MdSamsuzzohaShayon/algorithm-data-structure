from typing import Any, List


class Node:
    def __init__(self, val: Any):
        self.val: Any = val
        self.next: Node | None = None

    def __repr__(self):
        return f"<Node: {self.val}>"


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.size: int = 0

    def prepend(self, element: Any) -> None:
        # Insert at the beginning
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def append(self, element: Any) -> None:
        # Insert at the end
        new_node = Node(element)
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        self.size += 1

    def insert(self, element: Any, index: int = 0) -> None:
        new_node = Node(element)
        if index == 0:
            self.prepend(new_node)
        else:
            curr: Node | None = self.head
            pos: int = index
            while pos > 1:
                curr = curr.next
                pos -= 1

            prev_node = curr
            next_node = curr.next

            prev_node.next = new_node
            new_node.next = next_node

        self.size += 1

    def remove_from_front(self):
        removed_node: Node | None = self.head
        if self.head:
            self.head = self.head.next
            self.size -= 1

        return removed_node

    def remove_from_end(self) -> None | Node:
        removed_node: Node | None = self.head
        curr: Node | None = self.head
        prev: Node | None = None
        while curr:
            if not curr.next:
                removed_node = curr
                prev.next = None
            else:
                prev = curr
            curr = curr.next

        return removed_node

    def remove_from(self, index: int) -> None | Node:
        remove_node: Node | None = None

        if self.size == 0 or index >= self.size:
            remove_node = None
        elif index == 0:
            self.head = self.head.next
        else:
            prev: Node | None = None
            curr: Node | None = self.head
            pos: int = 0
            while curr:
                if pos == index and prev:
                    prev.next = curr.next
                    remove_node = curr
                    break
                pos += 1
                prev = curr
                curr = curr.next

        if remove_node:
            self.size -= 1
        return remove_node

    def is_empty(self) -> bool:
        return self.head is None

    def __repr__(self):
        nodes: List[Node] = []

        curr: Node | None = self.head
        while curr:
            if curr == self.head:
                nodes.append("[Head: %s]" % curr.val)
            elif curr.next is None:
                nodes.append("[Tail: %s]" % curr.val)
            else:
                nodes.append("[%s]" % curr.val)

            curr = curr.next

        return "-> ".join(nodes)


l = LinkedList()
l.prepend(10)
l.prepend(50)
l.prepend(20)
l.prepend(45)
l.prepend(49)
l.prepend(36)
l.append(60)
l.append(80)
l.insert(75, 4)
print(l)
l.remove_from(0)
l.remove_from(20)
l.remove_from(4)
l.remove_from(6)
print(l)
l.remove_from_front()
l.remove_from_end()
print(l)
