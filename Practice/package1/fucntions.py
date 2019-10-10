def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        max = number if number > max else max
    return max


def find_min(numbers):
    min = numbers[0]
    for number in numbers:
        min = number if number < min else min
    return min
