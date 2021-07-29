def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


if __name__ == "__main__":
    my = [35, 44, 50, 79, 103, 153, 1002, 55034, 3000005, 7000000]
    print(binary_search(my, 79, 0, len(my) - 1))
