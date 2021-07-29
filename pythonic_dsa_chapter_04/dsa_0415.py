"""Non-recursive binary search"""


def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False


if __name__ == "__main__":
    numbers = [35, 44, 50, 79, 103, 153, 1002, 55034, 3000005, 7000000]
    for number in [-10, 44, 40, 103, 110, 1002, 800, 55034]:
        print(binary_search_iterative(numbers, number))
