"""
https://www.youtube.com/watch?v=ngNJps_RUg8&list=PLC3y8-rFHvwjPxNAKvZpdnsr41E0fCMMP&index=45

A circular queue is a data structure that is similar to a regular queue,
but the last element is connected to the first element, forming a circle-like structure.
This solves the major limitation of the normal queue, where after a bit of insertion and deletion,
there will be non-usable empty space 1.

Here is an example implementation of a circular queue in Python using arrays 1:

Usage:
    Clock
    Streaming data
    Traffic lights
"""


class CurcularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
