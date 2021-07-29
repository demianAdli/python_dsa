from pythonic_dsa_chapter_07.dsa_0715_positional_list import *


class Item:
    slots = 'value', 'count'  # streamline memory usage

    def __init__(self, e):
        self.value = e  # the user s element
        self.count = 0  # access count initially zero


class FavoritesList:
    """List of elements ordered from most frequently accessed to least."""
    def find_position(self, e):
        """Search for element e and return its Position (or None if not found)."""
        walk = self.data.first()
        while walk is not None and walk.element().value != e:
            walk = self.data.after(walk)
        return walk

    def move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p != self.data.first():          # consider moving...
            cnt = p.element().count
            walk = self.data.before(p)
            if cnt > walk.element().count:      # must shift forward
                while (walk != self.data.first() and
                       cnt > self.data.before(walk).element().count):
                    walk = self.data.before(walk)
                self.data.add_before(walk, self.data.delete(p))     # delete/reinsert

    def __init__(self):
        """Create an empty list of favorites."""
        self.data = PositionalList()            # will be list of Item instances

    def __len__(self):
        """Return number of entries on favorites list."""
        return len(self.data)

    def is_empty(self):
        """Return True if list is empty."""
        return len(self.data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self.find_position(e)               # try to locate existing element
        if p is None:
            p = self.data.add_last(Item(e))     # if new, place at end
        p.element().count += 1                  # always increment count
        self.move_up(p)                         # consider moving forward

    def remove(self, e):
        """Remove element e from the list of favorites."""
        p = self.find_position(e)               # try to locate existing element
        if p is not None:
            self.data.delete(p)         # delete, if found

    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        walk = self.data.first()
        for j in range(k):
            item = walk.element()       # element of list is Item
            yield item.value           # report user’s element
            walk = self.data.after(walk)

    def __str__(self):
        return " ".join("(" + str(each.value) +
                        ", " + str(each.count) + ")"
                        for each in self.data)


if __name__ == "__main__":
    fav = FavoritesList()
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

    # Since top method is a generator, we cast it to a list:
    print("Top 3:", list(fav.top(3)))
    # Or we can use the join method:
    print("Top 5:", ', '.join(str(each) for each in fav.top(5)))
    print(fav)

