from pythonic_dsa_chapter_08.dsa_0801_abc_tree import *


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # --------------------- additional abstract methods ---------------------
    @abstractmethod
    def left(self, p):
        """Return a Position representing p s left child.

        Return None if p does not have a left child.
        """
        pass

    @abstractmethod
    def right(self, p):
        """Return a Position representing p s right child.

        Return None if p does not have a right child.
        """
        pass

    # ---------- concrete methods implemented in this class ----------
    def sibling(self, p):
        """Return a Position representing p s sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:                  # p must be the root
            return None                     # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)   # possibly None
            else:
                return self.left(parent)    # possibly None

    def children(self, p):
        """Generate an iteration of Positions representing p s children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self.subtree_inorder(self.roots()):
                yield p

    def subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p.
           24 August, 2020
           Has been added later from Code Fragment 8.21.
        """
        if self.left(p) is not None:    # if left child exists, traverse its subtree
            for other in self.subtree_inorder(self.left(p)):
                yield other
        yield p     # visit p between its subtrees
        if self.right(p) is not None:   # if right child exists, traverse its subtree
            for other in self.subtree_inorder(self.right(p)):
                yield other

    def positions(self):
        """Generate an iteration of the tree s positions.
           24 August, 2020
           Has been added later from Code Fragment 8.22.
           - One can comment the whole current method which is
           an override of Tree.positions() or use the super() instead
           of return statement.
        """
        return self.inorder()   # make inorder the default
