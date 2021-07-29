from random import randrange
from pythonic_dsa_chapter_10.dsa_1002_map_base import *


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map."""
        self.table = cap * [None]
        self.n = 0              # number of entries in the map
        self.prime = p          # prime for MAD compression
        self.scale = 1 + randrange(p - 1)     # scale from 1 to p-1 for MAD
        self.shift = randrange(p)   # shift from 0 to p-1 for MAD

    def hash_function(self, k):
        return (hash(k) * self.scale + self.shift) % self.prime % len(self.table)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        j = self.hash_function(k)
        return self.bucket_getitem(j, k)                # may raise KeyError

    def __setitem__(self, k, v):
        j = self.hash_function(k)
        self.bucket_setitem(j, k, v)                    # subroutine maintains self.n
        if self.n > len(self.table) // 2:             # keep load factor <= 0.5
            self.resize(2 * len(self.table) - 1)       # number 2ˆx - 1 is often prime

    def __delitem__(self, k):
        j = self.hash_function(k)
        self.bucket_delitem(j, k)       # may raise KeyError
        self.n -= 1

    def resize(self, c):                # resize bucket array to capacity c
        old = list(self.items())        # use iteration to record existing items
        self.table = c * [None]         # then reset table to desired capacity
        self.n = 0                      # n recomputed during subsequent adds
        for k, v in old:
            self[k] = v                 # reinsert old key-value pair


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def bucket_getitem(self, j, k):
        bucket = self.table[j]
        if bucket is None:
            raise KeyError("Key Error:" + repr(k))  # no match found
        return bucket[k]                            # may raise KeyError

    def bucket_setitem(self, j, k, v):
        if self.table[j] is None:
            self.table[j] = UnsortedTableMap()  # bucket is new to the table
        oldsize = len(self.table[j])
        self.table[j][k] = v
        if len(self.table[j]) > oldsize:        # key was new to the table
            self.n += 1                         # increase overall map size

    def bucket_delitem(self, j, k):
        bucket = self.table[j]
        if bucket is None:
            raise KeyError("Key Error:" + repr(k))  # no match found
        del bucket[k]       # may raise KeyError

    def __iter__(self):
        for bucket in self.table:
            if bucket is not None:      # a nonempty slot
                for key in bucket:
                    yield key

    def __str__(self):
        return "{" + ', '.join(str(each) + ": " + str(self[each])
                               for each in self) + "}"


if __name__ == "__main__":
    my_map = ChainHashMap()
    print(len(my_map))
    print(len(my_map.table))
    my_map["B"] = 13
    my_map["C"] = 15
    my_map["D"] = 133
    print(my_map)
    # my_map["E"] = 11
    # my_map["F"] = 1132
    # my_map["G"] = 9
    # my_map["H"] = 4
    # my_map["I"] = 2
    # my_map["J"] = 41
    # my_map["K"] = 13
    # print(my_map["E"])
    # print(len(my_map))
