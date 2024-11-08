# Calculate the mean, standard deviation, and sum of the 3x3 array elements.

import numpy as np


def calculate_stats(arr):
    # Flatten the 2D list into a 1D list
    flattened_arr = [element for row in arr for element in row]

    # Calculate mean
    mean = sum(flattened_arr) / len(flattened_arr)

    # Calculate standard deviation
    std_dev = (
        sum((element - mean) ** 2 for element in flattened_arr) / len(flattened_arr)
    ) ** 0.5

    # Calculate sum of elements
    sum_elements = sum(flattened_arr)

    return mean, std_dev, sum_elements


# test function

arr = np.random.randint(1, 101, size=(3, 3))
mean, std_dev, sum_elements = calculate_stats(arr)

print(f"{arr}\n")
print(
    f"mean of array: {mean},\nstd_dev of array: {std_dev},\nsum of array: {sum_elements}"
)
