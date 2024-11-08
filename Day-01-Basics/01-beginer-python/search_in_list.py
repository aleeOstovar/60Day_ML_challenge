# find min, max,and average of a list of numbers


def find_min_max_avg(numbers):
    min_num = numbers[0]
    max_num = numbers[0]
    total = 0

    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
        total += num

    avg_num = total / len(numbers)

    return min_num, max_num, avg_num


numbers = [2, 5, -5, 4, 8, 22, 48, -28]

min_num, max_num, avg_num = find_min_max_avg(numbers)
print(f"min: ${min_num}\nmax: ${max_num}\navg: ${avg_num}")
