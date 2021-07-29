from pythonic_dsa_chapter_09.dsa_0901_priority import Item
from queue import Empty


class HeapPriorityQueue:        # base class defines Item
    """A min-oriented priority queue implemented with a binary heap."""

    def is_empty(self):         # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0

    def parent(self, j):
        return (j - 1) // 2

    def left(self, j):
        return 2 * j + 1

    def right(self, j):
        return 2 * j + 2

    def has_left(self, j):
        return self.left(j) < len(self.data)    # index beyond end of list?

    def has_right(self, j):
        return self.right(j) < len(self.data)   # index beyond end of list?

    def swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def upheap(self, j):
        """
        31 August, 2020
        be aware of Item instances are being compared just based on
        their value, so self.data[j] < self.data[parent just copmaring
        their values.
        """
        parent = self.parent(j)
        if j > 0 and self.data[j] < self.data[parent]:
            self.swap(j, parent)
            self.upheap(parent)         # recur at position of parent

    def downheap(self, j):
        if self.has_left(j):
            left = self.left(j)
            small_child = left          # although right may be smaller
            if self.has_right(j):
                right = self.right(j)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self. data[small_child] < self.data[j]:
                self.swap(j, small_child)
                self.downheap(small_child)      # recur at position of small child

    def __init__(self, contents=()):
        """Create a new priority queue.
        By default, queue will be empty. If contents is given, it should be as an
        iterable sequence of (k,v) tuples specifying the initial contents.
        """
        self.data = [Item(k, v) for k, v in contents]  # empty by default
        if len(self.data) > 1:
            self.heapify()

    def heapify(self):
        start = self.parent(len(self) - 1)  # start at PARENT of last leaf
        for j in range(start, -1, -1):  # going to and including the root
            self.downheap(j)

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self. data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self.data.append(Item(key, value))
        self.upheap(len(self.data) - 1)         # upheap newly added position

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self.data[0]
        return item.key, item.value

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        self.swap(0, len(self.data) - 1)    # put minimum item at the end
        item = self.data.pop()              # and remove it from the list;
        self.downheap(0)                   # then fix new root
        return item.key, item.value

    def __str__(self):
        return ', '.join('(' + str(each.key) + ', ' + str(each.value) + ')'
                         for each in self.data)


if __name__ == "__main__":
    heap = HeapPriorityQueue(((3, 10), (5, 25), (7, 170),
                              (10, 210), (11, 110), (14, 140), (17, 117)))
    print(heap)

    heap_1 = HeapPriorityQueue(((10, 210), (3, 10), (14, 140),
                                (5, 25), (11, 110), (17, 117), (7, 170)))
    print(heap_1)




