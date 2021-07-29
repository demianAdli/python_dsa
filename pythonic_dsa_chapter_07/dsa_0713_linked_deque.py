"""
LinkedDeque class from dsa
11 August, 2020
"""
from pythonic_dsa_chapter_07.dsa_0712_doubly_base import *


class LinkedDeque(DoublyLinkedBase):
    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.header.next_one.element     # real item just after header

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.trailer.prev.element  # real item just before trailer

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self.insert_between(e, self.header, self.header.next_one)  # after header

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self.insert_between(e, self.trailer.prev, self.trailer)  # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.delete_node(self.header.next_one)  # use inherited method

    def delete_last(self):
        """Remove and return the element from the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.delete_node(self.trailer.prev)  # use inherited method





