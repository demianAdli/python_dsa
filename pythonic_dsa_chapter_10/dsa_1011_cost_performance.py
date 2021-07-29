"""
September 22, 2020
I've just changed the name of underlying SortedTableMap from _M to _base
"""
from pythonic_dsa_chapter_10.dsa_1008_analysis_02 import *


class CostPerformanceDatabase:
    """Maintain a database of maximal (cost,performance) pairs."""

    def __init__(self):
        """Create an empty database."""
        self._base = SortedTableMap()   # or a more efficient sorted map

    def best(self, c):
        """Return (cost,performance) pair with largest cost not exceeding c.

        Return None if there is no such pair.
        """
        return self._base.find_le(c)

    def add(self, c, p):
        """Add new entry with cost c and performance p."""
        # determine if (c,p) is dominated by an existing pair
        other = self._base.find_le(c)   # other is at least as cheap as c
        if other is not None and other[1] >= p:  # if its performance is as good,
            return          # (c,p) is dominated, so ignore
        self._base[c] = p      # else, add (c,p) to database
        # and now remove any pairs that are dominated by (c,p)
        other = self._base.find_gt(c)   # other more expensive than c
        while other is not None and other[1] <= p:
            del self._base[other[0]]
            other = self._base.find_gt(c)

    def __str__(self):
        return str(self._base)


if __name__ == "__main__":
    carshop = CostPerformanceDatabase()
    carshop.add(900, 100)
    carshop.add(800, 100)
    carshop.add(1000, 140)
    carshop.add(2000, 130)
    carshop.add(500, 90)
    carshop.add(801, 90)
    print(carshop)