from time import time


def compute_average(n):
    """Perform n appends to an empty list and return average time elapsed."""
    data = []
    start = time()              # record the start time (in seconds)
    for k in range(n):
        data.append(None)
    end = time()                # record the end time (in seconds)
    return (end - start) / n    # compute average per operation


print(compute_average(10))
print(compute_average(100))
print(compute_average(1000))
print(compute_average(100000))
print(compute_average(10000000))