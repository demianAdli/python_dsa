from pythonic_dsa_chapter_09.dsa_0904_heap import *


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""

# ------------------------------ nested Locator class ------------------------------
    class Locator(Item):
        """Token for locating an entry of the priority queue."""
        __slots__ = 'index'     # add index as additional field

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self.index = j

# ------------------------------ nonpublic behaviors ------------------------------
    # override swap to record new indices
    def swap(self, i, j):
        super().swap(i, j)          # perform the swap
        self.data[i].index = i    # reset locator index (post-swap)
        self.data[j].index = j    # reset locator index (post-swap)

    def bubble(self, j):
        if j > 0 and self.data[j] < self.data[self.parent(j)]:
            self.upheap(j)
        else:
            self.downheap(j)

    def add(self, key, value):
        """Add a key-value pair."""
        token = self.Locator(key, value, len(self.data))    # initiaize locator index
        self.data.append(token)
        self.upheap(len(self.data) - 1)
        return token

    def update(self, loc, newkey, newval):
        """Update the key and value for the entry identified by Locator loc."""
        j = loc.index
        if not (0 <= j < len(self) and self.data[j] is loc):
            raise ValueError("Invalid locator")
        loc.key = newkey
        loc.value = newval
        self.bubble(j)

    def remove(self, loc):
        """Remove and return the (k,v) pair identified by Locator loc."""
        j = loc.index
        if not (0 <= j < len(self) and self.data[j] is loc):
            raise ValueError("Invalid locator")
        if j == len(self) - 1:              # item at last position
            self.data.pop()                 # just remove it
        else:
            self.swap(j, len(self) - 1)     # swap item to the last position
            self.data.pop()                 # remove it from the list
            self.bubble(j)                  # fix item displaced by the swap
        return loc.key, loc.value
