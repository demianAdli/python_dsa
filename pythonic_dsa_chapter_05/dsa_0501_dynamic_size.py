"""
Illustrating the effect of Python's list dynamic behavior
on the memory size; doubles when needed.
"""


import sys
data = []

for k in range(10):
    length = len(data)
    size = sys.getsizeof(data)     # size in bytes
    print("Length: {0:3d}\t\t Size in bytes: {1:4d}".format(length, size))
    data.append(None)
