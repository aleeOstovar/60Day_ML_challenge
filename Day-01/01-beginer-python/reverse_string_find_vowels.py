# Reverse a string and count the number of vowels in it.


def reverse_string(string):
    return string[::-1]


def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        for vowel in vowels:
            if char == vowel:
                count += 1
    return count


text = "this is a sample text with a unique number of vowels"
reverse_string = reverse_string(text)
num_vowels = count_vowels(reverse_string)
print("reverse:\n\t", reverse_string, "\n")
print("total vowels:\n\t", num_vowels, "\n")
