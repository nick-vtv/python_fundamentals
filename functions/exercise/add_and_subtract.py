def add_and_subtract(a, b, c):
    sum_of_numbers = sum_numbers(a, b)
    result = subtract(sum_of_numbers, c)
    return result


def sum_numbers(a, b):
    return a + b


def subtract(c, d):
    return c - d


number_a = int(input())
number_b = int(input())
number_c = int(input())

final_result = add_and_subtract(number_a, number_b, number_c)

print(final_result)
