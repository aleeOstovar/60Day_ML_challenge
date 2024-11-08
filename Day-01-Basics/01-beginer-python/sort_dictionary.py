# Sort a dictionary by values and by keys.


def sort_dictionary(input_dict, by):
    sorted_dict = input_dict
    if by == "values":
        sorted_dict = dict(sorted(input_dict.items(), key=lambda x: x[1]))
    elif by == "keys":
        sorted_dict = dict(sorted(input_dict.items(), key=lambda x: x[0]))

    return sorted_dict


# Test the function

input_dict = {"apple": 2, "banana": 4, "cherry": 1, "date": 3}
sorted_dict_values = sort_dictionary(input_dict, "values")
sorted_dict_keys = sort_dictionary(input_dict, "keys")

print("Sorted by values:", sorted_dict_values)

print("Sorted by keys:", sorted_dict_keys)
