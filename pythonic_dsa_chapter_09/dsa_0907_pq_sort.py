from pythonic_dsa_chapter_09.dsa_0906_bottom_up import *
from pythonic_dsa_chapter_07.dsa_0715_positional_list import *


def pq_sort(positional_list):
    """Sort a collection of elements stored in a positional list."""
    length = len(positional_list)
    heap_pri_que = HeapPriorityQueue()
    for j in range(length):
        element = positional_list.delete(positional_list.first())
        heap_pri_que.add(element, element)     # use element as key and value
    for j in range(length):
        k, v = heap_pri_que.remove_min()
        positional_list.add_last(v)   # store smallest remaining element in C


pl = PositionalList()
pl.add_first(13)
pl.add_after(pl.first(), 19)
pl.add_after(pl.first(), 23)
pl.add_before(pl.last(), 17)
pl.add_after(pl.after(pl.first()), 40)
x = pl.add_before(pl.before(pl.last()), 85)
pl.add_before(x, 1500)
print(pl)
pq_sort(pl)
print(pl)