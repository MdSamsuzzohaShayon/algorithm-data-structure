from typing import List, Any
from collections import deque

"""
YouTube: https://www.youtube.com/watch?v=IxQHWt0GpsU
"""

# First In, First Out (FIFO)
class Queue:

    def __init__(self):
        self._items: List[Any] = []

    def enqueue(self, element: Any) -> None:
        self._items.append(element)

    def dequeue(self) -> Any:
        self._items.pop(0)

    def peek(self):
        return None if len(self._items) == 0 else self._items[0]


queue = Queue()
queue.enqueue()