def progress(x):
    progress_bar_list = []
    full_part = x // 10
    empty_part = 10 - full_part
    for full in range(1, full_part + 1):
        progress_bar_list.append('%')
    for empty in range(1, empty_part + 1):
        progress_bar_list.append('.')
    return progress_bar_list


int_number = int(input())
if int_number == 100:
    print(f'{int_number}% Complete!')
    print(f'[{"".join(progress(int_number))}]')
else:
    print(f'{int_number}% [{"".join(progress(int_number))}]')
    print('Still loading...')
