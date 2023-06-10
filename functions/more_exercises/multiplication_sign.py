def multiplication(a, b, c):
    if a == 0 or b == 0 or c == 0:
        result = 'zero'
    elif a < 0 and b < 0 and c < 0:
        result = 'negative'
    elif a < 0 < c and b > 0:
        result = 'negative'
    elif b < 0 < a and c > 0:
        result = 'negative'
    elif c < 0 < a and b > 0:
        result = 'negative'
    else:
        result = 'positive'
    return result


integer_a = int(input())
integer_b = int(input())
integer_c = int(input())
print(multiplication(integer_a, integer_b, integer_c))
