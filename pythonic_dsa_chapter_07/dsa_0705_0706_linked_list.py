"""
09 August, 2020
From the DSA book with very little changes

"Most Python developers do not nest classes,
so when you do so you break convention and increase maintenance cost."
From StackOverFlow
"""
from queue import Empty


class SinglyLinkedList:
    # -------------------------- nested Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = 'element', 'next_one'  # streamline memory usage

        def __init__(self, element, next_one):      # initialize node’s fields
            self.element = element              # reference to user’s element
            self.next_one = next_one

    # ------------------------------- stack methods --------------------------
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.head = self._Node(item, self.head)
        self.size += 1

    def top(self):
        if self.is_empty():
            raise Empty("The stack is empty")
        return self.head.element

    def pop(self):
        if self.is_empty():
            raise Empty("The stack is empty")
        answer = self.head.element
        self.head = self.head.next_one
        self.size -= 1
        return answer


if __name__ == "__main__":
    linked = SinglyLinkedList()
    linked.push(17)
    linked.push(23)
    print("head:", linked.head.element)
    print("size:", linked.size)
    linked.pop()
    print("head:", linked.head.element)



