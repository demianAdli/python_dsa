"""
29 August, 2020; read explanation of dsa_0901
"""
from pythonic_dsa_chapter_07.dsa_0715_positional_list import *
from pythonic_dsa_chapter_09.dsa_0901_priority import Item


class SortedPriorityQueue:  # base class defines Item
    """A min-oriented priority queue implemented with a sorted list."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self.data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self. data)

    def is_empty(self):
        """Return True if the priority queue is empty."""
        return len(self) == 0

    def add(self, key, value):
        """Add a key-value pair."""
        newest = Item(key, value)   # make new item instance
        walk = self.data.last()     # walk backward looking for smaller key
        while walk is not None and newest < walk.element():
            walk = self.data.before(walk)
        if walk is None:
            self.data.add_first(newest)     # new key is smallest
        else:
            self.data.add_after(walk, newest)   # newest goes after walk

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        p = self.data.first()
        item = p.element()
        return item.key, item.value

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self.data.delete(self.data.first())
        return item.key, item.value
