import ctypes                                       # provides low-level arrays
"""
22 July, 2020
This file gets together code fragments 3, 5 and 6 of the chapter.
1. length and capacity attributes have to be defined private,
as any changes in them block the class applicabality

2. I added __str__ method
"""


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        """Create an empty array."""
        self._n = 0                                 # count actual elements
        self._capacity = 1                          # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]                       # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:           # not enough room
            self._resize(2 * self._capacity)    # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                       # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)                 # new (bigger) array
        for k in range(self._n):                # for each existing value
            B[k] = self._A[k]
        self._A = B                              # use the bigger array
        self._capacity = c

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:            # not enough room
            self._resize(2 * self._capacity)     # so double capacityy
        for j in range(self._n, k, -1):          # shift rightmost first
            self._A[j] = self._A[j - 1]
        self._A[k] = value                       # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:                 # found a match!
                for j in range(k, self._n - 1):     # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None         # help garbage collection
                self._n -= 1                        # we have one less item
                return                              # exit immediately
        raise ValueError("value not found")         # only reached if no match

    def _make_array(self, c):                    # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()          # see ctypes documentation

    def __str__(self):
        return "[" + ", ".join([str(self._A[each]) for each in range(self._n)]) + "]"


if __name__ == "__main__":
    my = DynamicArray()
    my.append(10)
    my.append(33)
    my.append(13)
    my.append(29)
    # print(my)
    # print(" ".join([str(each) for each in my]))
    my.insert(2, 17)
    print(my)
    # print(" ".join([str(each) for each in my]))
    my.insert(0, 0)
    my.insert(6, 199)
    my.insert(6, 1)
    print(my)
    my.remove(13)
    print(my)


