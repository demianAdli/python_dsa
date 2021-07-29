"""
22 August, 2020
Implementation of nested classes
Code fragments 8.01-8.08
"""

from abc import abstractmethod, ABC


class Tree(ABC):
    """Abstract base class representing a tree structure."""

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
    # ---------- abstract methods that concrete subclass must support ----------

    @abstractmethod
    def root(self):
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
        return self.root() == p

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
            p = self.root()
        return self.hight_2(p)  # start height2 recursion


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


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    class Node:  # Lightweight, nonpublic class for storing a node.
        __slots__ = 'element', 'parent', 'left', 'right'

        def __init__(self, element, parent=None, left=None, right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

        def __str__(self):
            # x = "itself"
            return f"element: {self.element}"
# f"parent: {self.parent.element}\n"
# f"left: {x if self.}"

    class Position(BinaryTree.Position):
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

        def __str__(self):
            return str(self.node)

    def validate(self, p):
        """Return associated node, if position is valid."""

        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p.container is not self:
            raise ValueError("p does not belong to this container")
        if p.node.parent is p.node:  # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p.node

    def make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

# -------------------------- binary tree constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self.root = None
        self.size = 0

# -------------------------- public accessors --------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self.size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self.make_position(self.root)

    def parent(self, p):
        """Return the Position of p s parent (or None if p is root)."""
        node = self.validate(p)
        return self.make_position(node.parent)

    def left(self, p):
        """Return the Position of p s left child (or None if no left child)."""
        node = self.validate(p)
        return self.make_position(node.left)

    def right(self, p):
        """Return the Position of p s right child (or None if no right child)."""
        node = self.validate(p)
        return self.make_position(node.right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self.validate(p)
        count = 0
        if node.left is not None:   # left child exists
            count += 1
        if node.right is not None:  # right child exists
            count += 1
        return count

    def add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.

        Raise ValueError if tree nonempty.
        """
        if self.root is not None:
            raise ValueError("Root exists")
        self.size = 1
        self.root = self.Node(e)
        return self.make_position(self.root)

    def add_left(self, p, e):
        """Create a new left child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self.validate(p)
        if node.left is not None:
            raise ValueError("Left child exists")
        self.size += 1
        node.left = self.Node(e, node)      # node is its parent
        return self.make_position(node.left)

    def add_right(self, p, e):
        """Create a new right child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self.validate(p)
        if node.right is not None:
            raise ValueError("Right child exists")
        self.size += 1
        node.right = self.Node(e, node)      # node is its parent
        return self.make_position(node.right)

    def replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self.validate(p)
        old = node.element
        node.element = e
        return old

    def delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self.validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children")
        child = node.left if node.left else node.right  # might be None
        if child is not None:
            child.parent = node.parent          # child s grandparent becomes parent
        if node is self.root:
            self.root = child       # child becomes root
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self.size -= 1
        node.parent = node      # convention for deprecated node
        return node.element

    def attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self.validate(p)
        if not self.is_leaf(p):
            raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):  # all 3 trees must be same type
            raise TypeError("Tree types must match")
        self.size += len(t1) + len(t2)
        if not t1.is_empty():       # attached t1 as left subtree of node
            t1.root.parent = node
            node.left = t1.root
            t1.root = None          # set t1 instance to empty
            t1.size = 0
        if not t2.is_empty():       # attached t2 as right subtree of node
            t2.root.parent = node
            node.right = t2.root
            t2.root = None          # set t2 instance to empty
            t2.size = 0


if __name__ == "__main__":
    tree = LinkedBinaryTree()
    # print(type(tree))
    grand = tree.add_root(64)
    tree.add_left(grand, 16)
    tree.add_right(grand, 32)
    print(tree.left(grand))