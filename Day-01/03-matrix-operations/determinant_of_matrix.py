# Calculate the determinant of each matrix.
import numpy as np

mat1 = np.random.randint(1, 101, size=(3, 3))
mat2 = np.random.randint(1, 101, size=(3, 3))

det_mat1 = np.linalg.det(mat1)
det_mat2 = np.linalg.det(mat2)

print(f"matrix1:\n{mat1}\n")
print(f"determinant matrix1:\n{det_mat1}\n")
print(f"matrix2:\n{mat2}\n")
print(f"determinant matrix2:\n{det_mat2}\n")
