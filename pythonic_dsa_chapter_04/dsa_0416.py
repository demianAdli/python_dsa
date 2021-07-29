"""
A non-recursive reverse function.
"""


def non_recursive_reverse(seq):
    start, stop = 0, len(seq)
    while start < stop - 1:
        seq[start], seq[stop - 1] = seq[stop - 1], seq[start]
        start, stop = start + 1, stop - 1


if __name__ == "__main__":
    names = ["ali", "raha", "sam", "sara", "lili", "john"]
    non_recursive_reverse(names)
    print(names)
    non_recursive_reverse(names)
    print(names)