# Element-wise addition, subtraction, and multiplication.
import numpy as np


def calculation(arr1, arr2):
    clc = {
        "sum": np.add(arr1, arr2),
        "sub": np.subtract(arr1, arr2),
        "mul": np.multiply(arr1, arr2),
    }
    return clc


arr1 = np.random.randint(1, 101, size=(3, 3))
arr2 = np.random.randint(1, 101, size=(3, 3))

result = calculation(arr1, arr2)

for operation, output in result.items():
    print(f"{operation}:\n{output}\n")
