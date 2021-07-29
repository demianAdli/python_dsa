from pythonic_dsa_chapter_07.dsa_0715_positional_list import *


def insertion_sort(positional_list):
    """Sort PositionalList of comparable elements into nondecreasing order."""
    if len(positional_list) > 1:                          # otherwise, no need to sort it
        marker = positional_list.first()
        while marker != positional_list.last():
            pivot = positional_list.after(marker)         # next item to place
            value = pivot.element()
            if value > marker.element():    # pivot is already sorted
                marker = pivot              # pivot becomes new marker
            else:                           # must relocate pivot
                walk = marker               # find leftmost item greater than value
                while walk != positional_list.first() and positional_list.before(walk).element() > value:
                    walk = positional_list.before(walk)
                positional_list.delete(pivot)
                positional_list.add_before(walk, value)   # reinsert value before walk


if __name__ == "__main__":
    positional = PositionalList()
    positional.add_last(2)
    positional.add_last(13)
    positional.add_last(59)
    positional.add_last(33)
    positional.add_last(41)
    positional.add_last(43)
    print(positional)
    insertion_sort(positional)
    print(positional)
