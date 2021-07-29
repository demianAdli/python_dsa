"""
10 September, 2020
Unlike my former approach, I followed the book's method of using a nested class
in order to avoid further complications of inheretng the MutableMapping.
I use ABC class of abc module to make the MapBase an official abc thus
avoid Pycharm warning.
"""
try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping


class MapBase(MutableMapping):
    """Our own abstract base class that includes an Item class."""

# ------------------------------- nested Item class -------------------------------

    class Item:
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = 'key', 'value'

        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __eq__(self, other):
            return self.key == other.key    # compare items based on their keys

        def __ne__(self, other):
            return not self == other        # opposite of eq

        def __lt__(self, other):
            return self.key < other.key     # compare items based on their keys

        def __str__(self):
            return f"{self.key}, {self.value}"


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map."""
        self.table = []     # list of Item’s

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self.table:
            if k == item.key:
                return item.value
        raise KeyError("Key Error:" + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self.table:
            if k == item.key:      # Found a match:
                item.value = v     # reassign value
                return              # and quit
        # did not find match for key
        self.table.append(self.Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self.table)):
            if k == self.table[j].key:      # Found a match:
                self.table.pop(j)           # remove item
                return                      # and quit
        raise KeyError("Key Error:" + repr(k))

    def __len__(self):
        """Return number of items in the map."""
        return len(self.table)

    def __iter__(self):
        """Generate iteration of the map s keys."""
        for item in self.table:
            yield item.key   # yield the KEY

    def __str__(self):
        return '{' + ', '.join(str(each.key) + ": " + str(each.value)
                               for each in self.table) + '}'


if __name__ == "__main__":
    my = UnsortedTableMap()
    print(my)
    print(len(my))
    my[1] = 10
    my[2] = 10
    print(my)
