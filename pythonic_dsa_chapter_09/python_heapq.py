from heapq import *

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapify(li)

# printing created heap
print("The created heap is : ", end="")
print(li)

letter = [*"hello"]
heapify(letter)
print(letter)
heapreplace(letter, "a")
print(letter)
heappushpop(letter, "b")
print(letter)
