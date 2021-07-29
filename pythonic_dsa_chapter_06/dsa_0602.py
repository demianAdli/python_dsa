"""
30 July, 2020
My code and the book's is very similar so I didn't copy the book's
"""


class Empty(Exception):
    pass


class Stack:
    def __init__(self):
        self.__stack = []

    def __len__(self):
        return len(self.__stack)

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Empty("The stack is empty")
        return self.__stack.pop()

    def is_empty(self):
        return not len(self.__stack)

    def top(self):
        if self.is_empty():
            raise Empty("The stack is empty")
        return self.__stack[-1]


if __name__ == "__main__":
    S = Stack()              # contents: [ ]
    S.push(5)                # contents: [5]
    S.push(3)                 # contents: [5, 3]
    print(len(S))                    # contents: [5, 3]; outputs 2
    print(S.pop())             # contents: [5]; outputs 3
    print(S.is_empty())             # contents: [5]; outputs False
    print(S.pop())             # contents: [ ]; outputs 5
    print(S.is_empty())          # contents: [ ]; outputs True
    S.push(7)           # contents: [7]
    S.push(9)               # contents: [7, 9]
    print(S.top())             # contents: [7, 9]; outputs 9
    S.push(4)                   # contents: [7, 9, 4]
    print(len(S))                # contents: [7, 9, 4]; outputs 3
    print(S.pop())             # contents: [7, 9]; outputs 4
    S.push(6)
    S.pop()
    S.pop()
    S.pop()
    S.pop()