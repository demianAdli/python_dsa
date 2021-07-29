"""
Move-to-front heuristic
"""

from pythonic_dsa_chapter_07.dsa_0718_favorites import *


class FavoritesListMTF(FavoritesList):
    """List of elements ordered with move-to-front heuristic."""

    # we override move up to provide move-to-front semantics
    def move_up(self, p):
        """Move accessed item at Position p to front of list."""
        if p != self.data.first():
            self.data.add_first(self.data.delete(p))   # delete/reinsert

    # we override top because list is no longer sorted
    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")

    # we begin by making a copy of the original list
        temp = PositionalList()
        for item in self.data: # positional lists support iteration
            temp.add_last(item)

    # we repeatedly find, report, and remove element with largest count
        for j in range(k):
            # find and report next highest from temp
            high_pos = temp.first()
            walk = temp.after(high_pos)
            while walk is not None:
                if walk.element().count > high_pos.element().count:
                    high_pos = walk
                walk = temp.after(walk)
                # we have found the element with highest count
            yield high_pos.element().value      # report element to user
            temp.delete(high_pos)                # remove from temp list


if __name__ == "__main__":
    fav = FavoritesListMTF()
    fav.access(19)
    fav.access(33)
    fav.access(20)
    fav.access(25)
    fav.access(1)
    fav.access(19)
    fav.access(33)
    fav.access(33)
    fav.access(2)
    fav.access(1)
    fav.access(10)
    fav.access(2)
    fav.access(70)
    print(list(fav.top(3)))
    print(fav)