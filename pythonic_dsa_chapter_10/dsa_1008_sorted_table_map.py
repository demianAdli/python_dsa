"""
September 21, 2020
I've added the find_le() method.
September 22
find_index() is actually 'protected' following the book's approach,
in this way, find_ge() and find_le() make more sense.
September 23
This file is now obsolete since its find_le() does not work properly.
For the errorless class open the dsa_1001_analysis_03
"""
from pythonic_dsa_chapter_10.dsa_1002_map_base import *


class SortedTableMap(MapBase):
    """Map implementation using a sorted table."""

# ----------------------------- nonpublic behaviors -----------------------------
    def _find_index(self, k, low, high):
        """Return index of the leftmost item with key greater than or equal to k.

        Return high + 1 if no such item qualifies.

        That is, j will be returned such that:
        all items of slice table[low:j] have key < k
        all items of slice table[j:high+1] have key >= k
        """
        if high < low:
            return high + 1         # no element qualifies
        else:
            mid = (low + high) // 2
            if k == self.table[mid].key:
                return mid                  # found exact match
            elif k < self.table[mid].key:
                return self._find_index(k, low, mid - 1)     # Note: may return mid
            else:
                return self._find_index(k, mid + 1, high)    # answer is right of mid

# ----------------------------- public behaviors -----------------------------
    def __init__(self):
        """Create an empty map."""
        self.table = []

    def __len__(self):
        """Return number of items in the map."""
        return len(self.table)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        j = self._find_index(k, 0, len(self.table) - 1)
        if j == len(self.table) or self.table[j].key != k:
            raise KeyError("Key Error:" + repr(k))
        return self.table[j].value

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        j = self._find_index(k, 0, len(self.table) - 1)
        if j < len(self.table) and self.table[j].key == k:
            self.table[j].value = v                 # reassign value
        else:
            self.table.insert(j, self.Item(k, v))    # adds new item

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        j = self._find_index(k, 0, len(self.table) - 1)
        if j == len(self.table) or self.table[j].key != k:
            raise KeyError("Key Error:" + repr(k))
        self.table.pop(j) # delete item

    def __iter__(self):
        """Generate keys of the map ordered from minimum to maximum."""
        for item in self.table:
            yield item.key

    def __reversed__(self):
        """Generate keys of the map ordered from maximum to minimum."""
        for item in reversed(self.table):
            yield item.key

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)."""
        if len(self.table) > 0:
            return self.table[0].key, self.table[0].value
        else:
            return None

    def find_max(self):
        """Return (key,value) pair with maximum key (or None if empty)."""
        if len(self.table) > 0:
            return self.table[-1].key, self.table[-1].value
        else:
            return None

    def find_ge(self, k):
        """Return (key,value) pair with least key greater than or equal to k."""
        j = self._find_index(k, 0, len(self.table) - 1)  # j s key >= k
        if j < len(self.table):
            return self.table[j].key, self.table[j].value
        else:
            return None

    def find_le(self, k):
        """Return (key,value) pair with least key greater than or equal to k."""
        j = self._find_index(k, 0, len(self.table) - 1)  # j s key >= k
        if j > 0 and self.table[j].key == k:
            return self.table[j].key, self.table[j].value
        if j > 0:
            return self.table[j - 1].key, self.table[j - 1].value
        else:
            return None

    def find_lt(self, k):
        """Return (key,value) pair with greatest key strictly less than k."""
        j = self._find_index(k, 0, len(self.table) - 1)  # j s key >= k
        if j > 0:
            return self.table[j - 1].key, self.table[j - 1].value  # Note use of j-1
        else:
            return None

    def find_gt(self, k):
        """Return (key,value) pair with least key strictly greater than k."""
        j = self._find_index(k, 0, len(self.table) - 1)  # j s key >= k
        if j < len(self.table) and self.table[j].key == k:
            j += 1  # advanced past match
        if j < len(self.table):
            return self.table[j].key, self.table[j].value
        else:
            return None

    def find_range(self, start, stop):
        """Iterate all (key,value) pairs such that start <= key < stop.

        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self.table) - 1)  # find first result
        while j < len(self.table) and (stop is None or self.table[j].key < stop):
            yield self.table[j].key, self.table[j].value
            j += 1

    def __str__(self):
        return '{' + ', '.join(str(each.key) + ": " + str(each.value)
                               for each in self.table) + '}'


if __name__ == "__main__":
    sorted_map = SortedTableMap()
    print(sorted_map)
    sorted_map[0] = 10
    sorted_map[2] = 30
    sorted_map[3] = 17
    sorted_map[9] = 74
    sorted_map[13] = 2
    sorted_map[5] = 1
    print(sorted_map)
    print(sorted_map[5])
    print(sorted_map.find_max())
    print(sorted_map.find_min())
    print(sorted_map.find_ge(12))
    print(sorted_map.find_gt(9))
    print(sorted_map.find_lt(3))