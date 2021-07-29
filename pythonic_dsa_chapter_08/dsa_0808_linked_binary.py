"""
22 August, 2020
-- First mistake: Book's has made a mistake by providing validate and
make_position methods in the Position class while it claims in page 318
that this code is replicating PositionalList of section 07.04 behavior
(This class defines validate and make_position methods in the body of
PositionalList which is the main class. I have tested it by making
objects). Thus LinkedBinaryTree has to do the same so I put make_position
and validate methods in the main class of the current file and I've tested
it successfully.

-- Second mistake: Book's use root for both the name of a key data member
and an important method. I think Python gets confused whenever one calls
the method and return a node or error. So I rename all root() methods
to roots() in dsa_0801, dsa_0807 (has not any) and dsa_0808 and the problem
has been solved.


 Like copying section seven codes, I haven't followed the approach of
making nested classes but I defined them independently in the same file
as the main class (here LinkedBinaryTree)
 I didn't define any methods as nonpublic though it can be
considered in future improvements.
"""

from pythonic_dsa_chapter_08.dsa_0807_binary_abc import *


class Node:  # Lightweight, nonpublic class for storing a node.
    __slots__ = 'element', 'parent', 'left', 'right'

    def __init__(self, element, parent=None, left=None, right=None):
        self.element = element
        self.parent = parent
        self.left = left
        self.right = right


class Position(Position):
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
        return str(self.node.element)


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

# -------------------------- binary tree constructor --------------------------
    def validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, Position):
            raise TypeError("p must be proper Position type")
        if p.container is not self:
            raise ValueError("p does not belong to this container")
        if p.node.parent is p.node:     # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p.node

    def make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return Position(self, node) if node is not None else None

    def __init__(self):
        """Create an initially empty binary tree."""
        self.root = None
        self.size = 0

# -------------------------- public accessors --------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self.size

    def roots(self):
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
        if node.left is not None:       # left child exists
            count += 1
        if node.right is not None:      # right child exists
            count += 1
        return count

    def add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.

        Raise ValueError if tree nonempty.
        """
        if self.root is not None:
            raise ValueError("Root exists")
        self.size = 1
        self.root = Node(e)
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
        node.left = Node(e, node)   # node is its parent
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
        node.right = Node(e, node)      # node is its parent
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

    def __str__(self):
        return " ".join(str(each) for each in self)


if __name__ == "__main__":
    tree = LinkedBinaryTree()
    print(tree)
    print(type(tree))
    grand = tree.add_root(64)

    dad = tree.add_left(grand, 16)
    mom = tree.add_right(grand, 32)
    dad_child_01 = tree.add_left(dad, 1)
    dad_child_02 = tree.add_right(dad, 2)
    mom_child_01 = tree.add_left(mom, 3)
    mom_child_02 = tree.add_right(mom, 4)
    print(tree)
    # # print(tree.left(mom))
    # # print(tree.num_children(grand))
    # print(tree.replace(dad, 13))
    # print(tree.size)
    # print(tree.delete(mom_child_01))
    # print(tree.delete(mom))
    # print(mom)
    # print(tree.root.element)
    # print(tree.left(tree.roots()))
    # print(tree.size)