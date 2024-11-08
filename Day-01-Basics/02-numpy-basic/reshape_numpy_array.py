# Reshape 3x3 array into a 1×9 and a 9×1 shape, then transpose it.
import numpy as np

np_array = np.random.randint(1, 101, size=(3, 3))

reshape9x1 = np_array.reshape((9, 1))
reshape1x9 = np_array.reshape((1, 9))
reshape9x1T = reshape9x1.T
reshape1x9T = reshape1x9.T

print(f"Original 3x3 array:\t {np_array}")
print(f"reshape to 9x1:\t {reshape9x1}")
print(f"reshape to 1x9:\t {reshape1x9}")
print(f"9x1 transpose:\t {reshape9x1T}")
print(f"1x9 transpose:\t {reshape1x9T}")
