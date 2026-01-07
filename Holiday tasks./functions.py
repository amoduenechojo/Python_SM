def string_length(s):
    return len(s)

word = "Vixen"
print(string_length(word))  # Output: 5










def longest_word(words):
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest, len(longest)




def find_min(numbers):
    if not numbers:
        return None

    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest


def first_last_two(s):
    if len(s) < 2:
        return ""

    return s[:2] + s[-2:]
print(first_last_two("spring"))   # spng
print(first_last_two("go"))       # gogo
print(first_last_two("a"))        # ""
print(first_last_two(""))         # ""

