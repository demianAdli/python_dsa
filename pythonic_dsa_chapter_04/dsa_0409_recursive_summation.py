"""
Summation of a list of numbers.
"""


def recursive_summation(list_nums):
    """my solution works for all the list"""
    if len(list_nums) == 0:
        return 0
    else:
        return recursive_summation(list_nums[:-1]) + list_nums[-1]


def linear_sum(numbers, n):
    """book: Returns the sum of the first n numbers of sequence numbers"""
    if n == 0:
        return 0
    else:
        return linear_sum(numbers, n - 1) + numbers[n-1]


if __name__ == "__main__":
    print(recursive_summation([10, 9, 20]))
    print(linear_sum([10, 9, 20], 3))