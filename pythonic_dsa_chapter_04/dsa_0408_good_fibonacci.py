"""
This is an efficient implementation of a recursive function
which returns a member of the Fibonacci sequence by its index and
predecessor member.
"""


def good_fibonacci(n):
    """It returns the nth fibonacci and its predecessor"""
    if n <= 1:
        return n, 0
    else:
        a, b = good_fibonacci(n-1)
        return a+b, a


if __name__ == "__main__":
    print(good_fibonacci(5))