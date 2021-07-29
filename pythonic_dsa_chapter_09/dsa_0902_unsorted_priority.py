"""
29 August, 2020
Firstly, following my approach in copying the book's code fragments, I
did not apply nested class concept in copying the implementation of the
Item class (dsa_0901).
Secondly, I did not use inheritance from PriorityQueueBase class (dsa_0901)
because I find it absurd to use inheritance instead of implementing a single
method (is_empty()).
"""

from pythonic_dsa_chapter_07.dsa_0715_positional_list import *
from pythonic_dsa_chapter_09.dsa_0901_priority import Item


class UnsortedPriorityQueue:
    """A min-oriented priority queue implemented with an unsorted list."""

    def is_empty(self):
        """Return True if the priority queue is empty."""
        return len(self) == 0

    def find_min(self):         # nonpublic utility
        """Return Position of item with minimum key."""
        if self.is_empty():     # is empty inherited from base class
            raise Empty("Priority queue is empty")
        small = self.data.first()
        walk = self.data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self.data.after(walk)
        return small

    def __init__(self):
        """Create a new empty Priority Queue."""
        self.data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self.data)

    def add(self, key, value):
        """Add a key-value pair."""
        self.data.add_last(Item(key, value))   # demian (change it)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        p = self.find_min()
        item = p.element()
        return item.key, item.value

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self.find_min()
        item = self.data.delete(p)
        return item.key, item.value
