"""
19 August, 2020
Beware; if Position class has been used with self, we should eliminate the
self since it is not a nested class in my implementation.
"""
from abc import abstractmethod, ABC
from pythonic_dsa_chapter_07.dsa_0707_0708_linked_queue import *


class Position(ABC):
    """An abstraction representing the location of a single element."""

    @abstractmethod
    def element(self):
        """Return the element stored at this Position."""
        pass

    @abstractmethod
    def __eq__(self, other):
        """Return True if other Position represents the same location."""
        pass

    def __ne__(self, other):
        """Return True if other does not represent the same location."""
        return not (self == other)  # opposite of eq


class Tree(ABC):
    """Abstract base class representing a tree structure."""
    # ---------- abstract methods that concrete subclass must support ----------
    @abstractmethod
    def roots(self):
        """Return Position representing the tree s root (or None if empty)."""
        pass

    @abstractmethod
    def parent(self, p):
        """Return Position representing p s parent (or None if p is root)."""
        pass

    @abstractmethod
    def num_children(self, p):
        """Return the number of children that Position p has."""
        pass

    @abstractmethod
    def children(self, p):
        """Generate an iteration of Positions representing p s children."""
        pass

    @abstractmethod
    def __len__(self):
        """Return the total number of elements in the tree."""
        pass

# ---------- concrete methods implemented in this class ----------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.roots() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def hight_2(self, p):  # time is linear in size of subtree
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.hight_2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.roots()
        return self.hight_2(p)  # start height2 recursion

    def __iter__(self):
        """Generate an iteration of the tree s elements.
           23 August, 2020
           Has been added later from Code Fragment 8.16.

           -- It won't work till adding the positions method
           which shall iterate over all the positions.
        """
        for p in self.positions():  # use same order as positions()
            yield p.element()

    def preorder(self):
        """Generate a preorder iteration of positions in the tree.
           23 August, 2020
           Has been added later from Code Fragment 8.17.
        """
        if not self.is_empty():
            for p in self.subtree_preorder(self.roots()):  # start recursion
                yield p

    def subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p.
           23 August, 2020
           Has been added later from Code Fragment 8.17.
        """
        yield p                                     # visit p before its subtrees
        for c in self.children(p):                  # for each child c
            for other in self.subtree_preorder(c):  # do preorder of c’s subtree
                yield other

    def positions(self):
        """Generate an iteration of the tree s positions.
           23 August, 2020
           Has been added later from Code Fragment 8.18.
           - It can also return postorder or breadthfirst
           based on the type of needed traversal, then it can
           replace by current return statement.
        """
        return self.preorder()

    def postorder(self):
        """Generate a postorder iteration of positions in the tree.
           24 August, 2020
           Has been added later from Code Fragment 8.19.
        """
        if not self.is_empty():
            for p in self.subtree_postorder(self.roots()):  # start recursion
                yield p

    def subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p.
           24 August, 2020
           Has been added later from Code Fragment 8.19.
        """
        for c in self.children(p):      # for each child c
            for other in self.subtree_postorder(c):     # do postorder of c’s subtree
                yield other             # yielding each to our caller
        yield p

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree.
           24 August, 2020
           Has been added later from Code Fragment 8.20.
        """
        if not self.is_empty():
            fringe = LinkedQueue()  # known positions not yet yielded
            fringe.enqueue(self.roots())    # starting with the root
            while not fringe.is_empty():
                p = fringe.dequeue()    # remove from front of the queue
                yield p     # report this position
                for c in self.children(p):
                    fringe.enqueue(c)   # add children to back of queue
