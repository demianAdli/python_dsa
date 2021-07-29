"""
the book implementation of a fast recursive
function by eliminating half of recursive computations.
Just works for positive powers.
"""


def power(num, n):
    if n == 0:
        return 1
    else:
        partial = power(num, n//2)
        result = partial * partial
        if n % 2 == 1:
            result *= num
        return result


if __name__ == "__main__":
    print(power(3, 2))
    print(power(3, 3))



