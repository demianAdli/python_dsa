"""
September 30, 2020
I just make an imaginary class to put three functions of the book
which all are a possible implementation for a Mutable Map.
*** It may need a specific underlying data structure so set can be a
wrong choice. ***

*** Read the book and add the correct underlying data structure
 (It is explained in few lines) ***
"""


# dsa_1014
class MutableMap:
    def __init__(self):
        """Just to avoid error in the main methods (to have a len)"""
        self.elements = set()

    def __len__(self):
        """Demian added it"""
        return len(self.elements)

    def add(self, item):
        """Demian added it"""
        self.elements.add(item)

    def __lt__(self, other): # supports syntax S < T
        """Return true if this set is a proper subset of other."""
        if len(self) >= len(other):
            return False # proper subset must have strictly smaller size
        for e in self.elements:     # #elements is added bye Demian
            if e not in other:
                return False    # not a subset since element missing from other
        return True

    # dsa_1015
    def __or__(self, other): # supports syntax S | T
        """Return a new set that is the union of two existing sets."""
        result = type(self)()   # create new instance of concrete class
        for e in self.elements:     # #elements is added bye Demian
            result.add(e)
        for e in other.elements:    # #elements is added bye Demian
            result.add(e)
        return result

    # dsa_1016
    def __ior__(self, other):   # supports syntax S |= T
        """Modify this set to be the union of itself an another set."""
        for e in other.elements:    # #elements is added bye Demian
            self.add(e)
        return self.elements    # #elements is added bye Demian
