"""
26 August, 2020

I removed below method from the body of EulerTour(ABC) after
that I've found out it does not help with anything. I also changed
tree().is_leaf call in ParenthesizeTour(EulerTour) to tree.is_leaf
thus running execute() wouldn't throw any exceptions.
    def tree(self):
        # Return reference to the tree being traversed.
        return self.tree
"""

from abc import ABC, abstractmethod


class EulerTour(ABC):
    """Abstract base class for performing Euler tour of a tree.

    hook previsit and hook postvisit may be overridden by subclasses.
    """
    def __init__(self, tree):
        """Prepare an Euler tour template for given tree."""
        self.tree = tree

    def execute(self):
        """Perform the tour and return any result from post visit of root."""
        if len(self.tree) > 0:
            return self.tour(self.tree.roots(), 0, [])     # start the recursion

    def tour(self, p, d, path):
        """Perform tour of subtree rooted at Position p.

        p Position of current node being visited
        d depth of p in the tree
        path list of indices of children on path from root to p
        """
        self.hook_previsit(p, d, path)      # ”pre visit” p
        results = []
        path.append(0)          # add new index to end of path before recursion
        for c in self.tree.children(p):
            results.append(self.tour(c, d + 1, path))   # recur on child s subtree
            path[-1] += 1       # increment index
        path.pop()                  # remove extraneous index from end of path
        answer = self.hook_postvisit(p, d, path, results)   # ”post visit” p
        return answer

    @abstractmethod
    def hook_previsit(self, p, d, path):    # can be overridden
        pass

    @abstractmethod
    def hook_postvisit(self, p, d, path, results):  # can be overridden
        pass


class PreorderPrintIndentedTour(EulerTour):
    def hook_previsit(self, p, d, path):
        print(2 * d * ' ' + str(p.element()))

    def hook_postvisit(self, p, d, path, results):
        """Just to avoid making it an abstract class"""
        pass


class PreorderPrintIndentedLabeledTour(EulerTour):
    def hook_previsit(self, p, d, path):
        label = '.'.join(str(j+1) for j in path)    # labels are one-indexed
        print(2 * d * ' ' + label, p.element())

    def hook_postvisit(self, p, d, path, results):
        """Just to avoid making it an abstract class"""
        pass


class ParenthesizeTour(EulerTour):
    def hook_previsit(self, p, d, path):
        if path and path[-1] > 0:   # p follows a sibling
            print(', ', end='')    # so preface with comma
        print(p.element(), end='')  # then print element
        if not self.tree.is_leaf(p):  # if p has children
            print(' (', end='')    # print opening parenthesis

    def hook_postvisit(self, p, d, path, results):
        if not self.tree.is_leaf(p):  # if p has children
            print(')', end='')      # print closing parenthesis


class DiskSpaceTour(EulerTour):
    def hook_previsit(self, p, d, path):
        """Just to avoid making it an abstract class"""
        pass

    def hook_postvisit(self, p, d, path, results):
        # we simply add space associated with p to that of its subtrees
        return p.element().space() + sum(results)


class BinaryEulerTour(EulerTour):
    """Abstract base class for performing Euler tour of a binary tree.

    This version includes an additional hook invisit that is called after the tour
    of the left subtree (if any), yet before the tour of the right subtree (if any).

    Note: Right child is always assigned index 1 in path, even if no left sibling.
    """
    def tour(self, p, d, path):
        results = [None, None]          # will update with results of recursions
        self.hook_previsit(p, d, path)  # ”pre visit” for p
        if self.tree.left(p) is not None:   # consider left child
            path.append(0)
            results[0] = self.tour(self.tree.left(p), d+1, path)
            path.pop()
        self.hook_invisit(p, d, path)           # ”in visit” for p
        if self.tree.right(p) is not None:     # consider right child
            path.append(1)
            results[1] = self.tour(self.tree.right(p), d+1, path)
            path.pop()
        answer = self.hook_postvisit(p, d, path, results)   # ”post visit” p
        return answer

    @abstractmethod
    def hook_invisit(self, p, d, path):
        pass        # can be overridden


class BinaryLayout(BinaryEulerTour):
    """Class for computing (x,y) coordinates for each node of a binary tree."""
    def __init__(self, tree):
        super().__init__(tree)      # must call the parent constructor
        self.count = 0              # initialize count of processed nodes

    def hook_previsit(self, p, d, path):
        """Just to avoid making it an abstract class"""
        pass

    def hook_invisit(self, p, d, path):
        p.element().setX(self.count)   # x-coordinate serialized by count
        p.element().setY(d)             # y-coordinate is depth
        self.count += 1                 # advance count of processed nodes

    def hook_postvisit(self, p, d, path, results):
        """Just to avoid making it an abstract class"""
        pass
