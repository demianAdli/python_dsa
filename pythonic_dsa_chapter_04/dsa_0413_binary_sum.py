"""
Computes summation of a set of numbers recursively.
"""


def binary_sum(seq, start, stop):
    """books's solution"""
    if start > stop:
        return 0
    elif start == stop - 1:
        return seq[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(seq, start, mid) + binary_sum(seq, mid, stop)


if __name__ == "__main__":
    numbers = [10, 20, 30, 40]
    print(binary_sum(numbers, 0, len(numbers)))
