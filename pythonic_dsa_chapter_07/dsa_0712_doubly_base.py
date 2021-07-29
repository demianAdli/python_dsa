"""
DoublyLinkedBase class from dsa
11 August, 2020
16 August, 2020
Update (added __str__)
In order to make a nicer Node __str__ we can use next and prev, to make
it happen, we should make header and trailer of DoublyLinkedBase private
members, so printing them does not make a problem
"""
from queue import Empty


class Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = 'element', 'prev', 'next_one'  # streamline memory usage

    def __init__(self, element, prev, next_one):    # initialize node’s fields
        self.element = element                  # reference to user’s element
        self.prev = prev
        self.next_one = next_one

    def __str__(self):
        return str(self.element)
        # return f"---------node\nelement: {self.element} \n" \
        #        f"next: {self.next_one}\nprevious: {self.prev}\n---------"


class DoublyLinkedBase:
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next_one = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = Node(e, predecessor, successor)   # linked to neighbors
        predecessor.next_one = newest
        successor.prev = newest
        self.size += 1
        return newest

    def delete_node(self, node):
        predecessor = node.prev
        successor = node.next_one
        predecessor.next_one = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.element
        node.prev = node.next_one = node.element = None
        return element


if __name__ == "__main__":
    doubly = DoublyLinkedBase()
    print(doubly.is_empty())
    # print(doubly.header)
    # print(doubly.trailer)
    doubly.insert_between(15, doubly.header, doubly.trailer)

    print(doubly)