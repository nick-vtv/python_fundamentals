from math import floor


def longer_line(a, b, c, d, e, f, g, h):
    first_line_x_sum = abs(a) + abs(c)
    first_line_y_sum = abs(b) + abs(d)
    second_line_x_sum = abs(e) + abs(g)
    second_line_y_sum = abs(f) + abs(h)
    first_line_max_diff = max(first_line_x_sum, first_line_y_sum)
    second_line_max_diff = max(second_line_x_sum, second_line_y_sum)
    if first_line_max_diff == second_line_max_diff:
        longest_line = first_line_max_diff
    else:
        longest_line = max(first_line_max_diff, second_line_max_diff)
    if longest_line == first_line_max_diff:
        return a, b, c, d
    else:
        return e, f, g, h


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
max_x1, max_y1, max_x2, max_y2 = longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
if max(abs(max_x1), abs(max_y1)) <= max(abs(max_x2), abs(max_y2)):
    print(f'({floor(max_x1)}, {floor(max_y1)})({floor(max_x2)}, {floor(max_y2)})')
else:
    print(f'({floor(max_x2)}, {floor(max_y2)})({floor(max_x1)}, {floor(max_y1)})')
