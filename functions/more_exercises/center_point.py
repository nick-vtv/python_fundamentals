from math import floor


def coordinate_closest_to_center(a, b, c, d):
    max_first_point = max(abs(a), abs(b))
    max_second_point = max(abs(c), abs(d))
    if max_first_point == max_second_point:
        min_point = max_first_point
    else:
        min_point = min(max_first_point, max_second_point)
    if min_point == max_first_point:
        return a, b
    else:
        return c, d


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
min_x, min_y = coordinate_closest_to_center(x1, y1, x2, y2)
print(f'({floor(min_x)}, {floor(min_y)})')
