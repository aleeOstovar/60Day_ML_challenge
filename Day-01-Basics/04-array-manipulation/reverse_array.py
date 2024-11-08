# reverse array
import numpy as np

arr = np.random.randint(1, 60, size=(20))

rev_arr = np.flip(arr).tolist()

print(f"input array:\n{arr}\n")
print(f"reverse of array:\n{rev_arr}\n")
