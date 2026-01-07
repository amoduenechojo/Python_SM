def find_min(numbers):
    if not numbers:
        return None

    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest
