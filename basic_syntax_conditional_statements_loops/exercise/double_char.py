while True:
    command = input()
    if command == 'End':
        break
    if command == 'SoftUni':
        continue
    for char in command:
        print(f'{char}{char}', end='')
    else:
        print()
