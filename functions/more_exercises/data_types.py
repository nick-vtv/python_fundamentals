def simple_logic(x, y):
    if x == 'int':
        print(int(y) * 2)
    elif x == 'real':
        print(f'{float(y) * 1.5:.2f}')
    elif x == 'string':
        print('$' + str(y) + '$')


data_type = input()
value = input()
simple_logic(data_type, value)
