from pythonic_dsa_chapter_07.dsa_0712_doubly_base import *


class Position:
    """An abstraction representing the location of a single element."""

    def __init__(self, container, node):
        """Constructor should not be invoked by user."""
        self.container = container
        self.node = node

    def element(self):
        """Return the element stored at this Position."""
        return self.node.element

    def __eq__(self, other):
        """Return True if other is a Position representing the same location."""
        return type(other) is type(self) and other.node is self.node

    def __ne__(self, other):
        """Return True if other does not represent the same location."""
        return not (self == other)  # opposite of eq

    def __str__(self):
        return f"----position\ncontainer: {self.container}" \
               f"\nNode: {self.node}\n----\n"


class PositionalList(DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""
    def validate(self, p):
        """Return position s node, or raise appropriate error if invalid."""
        if not isinstance(p, Position):
            raise TypeError("p must be proper Position type")
        if p.container is not self:
            raise ValueError("p does not belong to this container")
        if p.node.next_one is None:     # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p.node

    def make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self.header or node is self.trailer:
            return None  # boundary violation
        else:
            return Position(self, node)  # legitimate position

    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self.make_position(self.header.next_one)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self.make_position(self.trailer.prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self.validate(p)
        return self.make_position(node.prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self.validate(p)
        return self.make_position(node.next_one)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super().insert_between(e, predecessor, successor)
        return self.make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self.insert_between(e, self.header, self.header.next_one)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self.insert_between(e, self.trailer.prev, self.trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self.validate(p)
        return self.insert_between(e, original.prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self.validate(p)
        return self.insert_between(e, original, original.next_one)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self.validate(p)
        return self.delete_node(original)   # inherited method returns element

    def replace(self, p, e):
        """Replace the element at Position p with e.

        Return the element formerly at Position p.
        """
        original = self.validate(p)
        old_value = original.element   # temporarily store old element
        original.element = e            # replace with new element
        return old_value                # return the old element value

    def __str__(self):
        return ' '.join(str(each) for each in self)


if __name__ == "__main__":
    pl = PositionalList()
    # print(pl.header)
    print(pl.add_first(13))
    # print(pl.first().node)   # shows what Node class __str__ method returns
    # print(pl.first().node.prev)
    # print(pl.first().container)
    # print(type(pl.add_after(pl.first(), 19)))
    # print(type(pl.add_after(pl.first(), 19).container))
    print(pl.add_after(pl.first(), 19))
    # pl.add_after(Position(pl, 13), 23)
    pl.add_after(pl.first(), 23)
    pl.add_before(pl.last(), 17)
    pl.add_after(pl.after(pl.first()), 40)
    x = pl.add_before(pl.before(pl.last()), 85)
    print(x)
    pl.add_before(x, 1500)
    print(pl)
    # print(pl.last().container)
    # print(pl.first().container)
