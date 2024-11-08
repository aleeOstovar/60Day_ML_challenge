# extract even numbers from an array
import numpy as np


def evenExtractor(arr):
    evens = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            evens.append(arr[i])

    return evens


arr = np.random.randint(1, 60, size=(20)).tolist()
evens = evenExtractor(arr)

print(f"input array:\n{arr}\n")
print(f"evens in array:\n{evens}\n")
