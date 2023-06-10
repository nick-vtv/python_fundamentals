def calc_factorial(x):
    factorial = x
    for number in range(x - 1, 0, -1):
        factorial *= number
    return factorial


int_x = int(input())
int_y = int(input())

factorial_x = calc_factorial(int_x)
factorial_y = calc_factorial(int_y)

result = factorial_x / factorial_y

print(f'{result:.2f}')
