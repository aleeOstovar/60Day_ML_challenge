# numpy matrix multiplication.
import numpy as np

arr1 = np.random.randint(1, 101, size=(3, 3))
arr2 = np.random.randint(1, 101, size=(3, 3))

result = np.matmul(arr1, arr2)

print(f"matrix1:\n{arr1}\n")
print(f"matrix2:\n{arr2}\n")
print(result)
