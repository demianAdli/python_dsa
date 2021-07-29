"""
This function compute power of a value.
Book does not consider negative powers. I have
added negative powers to my implementation.
Because of its similar appearance to the factorial function,
I have named it 'powerial'.
"""


def powerial(num, n):
    """my solution for negative and positive n"""
    if n == 0:
        return 1
    elif n < 0:
        return 1 / num * powerial(num, n + 1)
    else:
        return num * powerial(num, n - 1)


if __name__ == "__main__":
    print(powerial(3, -2))
    print(3 ** -2)