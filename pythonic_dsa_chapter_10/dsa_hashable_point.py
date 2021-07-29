"""
September 15, 2020
I've used the Point class (which is a class for teaching purposes) to
examine the application of __hash__ method to make a hashable user-defined
object.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):   # class
        return cls(0, 0)

    def __str__(self):   # string
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __lt__(self, other):
        return not self.__ge__(other)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(other * self.x, other * self.y)

    def __hash__(self):
        return hash((self.x, self.y))


if __name__ == "__main__":
    point_01 = Point(2, 3)
    point_02 = Point(5, 5)
    point_03 = Point(5, 5)
    print(hash(point_03))




