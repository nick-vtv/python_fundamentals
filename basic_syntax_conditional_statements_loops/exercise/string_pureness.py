number_of_strings = int(input())
for string in range(number_of_strings):
    string_name = input()
    for char in string_name:
        if char == ',' or char == '.' or char == '_':
            print(f'{string_name} is not pure!')
            break
    else:
        print(f'{string_name} is pure.')
