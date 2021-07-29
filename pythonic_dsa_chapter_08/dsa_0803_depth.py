"""
20 August, 2020
All these functions have been added to the dsa_0801_abc_tree as
its methods
"""


def depth(self, p):
    """Return the number of levels separating Position p from the root."""
    if self.is_root(p):
        return 0
    else:
        return 1 + self.depth(self.parent(p))


def hight_2(self, p):   # time is linear in size of subtree
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
        p = self.root()
    return self.hight_2(p)  # start height2 recursion
