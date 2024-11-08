# extract every third element in an array
import numpy as np


def extract_3rd_element(arr):
    return arr[::3]


arr = np.random.randint(1, 60, size=(20)).tolist()

third_elements = extract_3rd_element(arr)

print(f"input array:\n{arr}\n")
print(f"extract every third element:\n{third_elements}\n")
