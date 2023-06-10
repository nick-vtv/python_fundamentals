def smallest_number(a, b, c):
    d = min(a, b, c)
    return d


number_a = int(input())
number_b = int(input())
number_c = int(input())
smallest_num = smallest_number(number_a, number_b, number_c)
print(smallest_num)
