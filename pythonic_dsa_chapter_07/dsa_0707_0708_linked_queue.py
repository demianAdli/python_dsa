"""
LinkedQueue class from dsa
10 August, 2020
I made the Node class an independent public one, as it is
more regular in Python coding.
I also made all the attributes public.
"""
from queue import Empty


class Node:
    """Lightweight class for storing a singly linked node."""
    __slots__ = 'element', 'next_one'  # streamline memory usage

    def __init__(self, element, next_one):  # initialize node’s fields
        self.element = element  # reference to user’s element
        self.next_one = next_one


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self.size = 0           # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self.size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self.size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.head.element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """

        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self.head.element
        self.head = self.head.next_one
        self.size -= 1
        if self.is_empty():             # special case as queue is empty
            self.tail = None            # removed head had been the tail
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = Node(e, None)          # node will be new tail node
        if self.is_empty():
            self.head = newest          # special case: previously empty
        else:
            self.tail.next_one = newest
        self.tail = newest             # update reference to tail node
        self.size += 1
