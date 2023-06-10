line_one_list = input().split()
line_two_list = input().split()
line_three_list = input().split()

player_wins = ''

if line_one_list.count('1') == 3 or line_two_list.count('1') == 3 or line_three_list.count('1') == 3:
    player_wins = 'First'
elif line_one_list.count('2') == 3 or line_two_list.count('2') == 3 or line_three_list.count('2') == 3:
    player_wins = 'Second'

elif line_one_list[0] == '1' and line_two_list[1] == '1' and line_three_list[2] == '1':
    player_wins = 'First'
elif line_one_list[2] == '1' and line_two_list[1] == '1' and line_three_list[0] == '1':
    player_wins = 'First'
elif line_one_list[0] == '2' and line_two_list[1] == '2' and line_three_list[2] == '2':
    player_wins = 'Second'
elif line_one_list[2] == '2' and line_two_list[1] == '2' and line_three_list[0] == '2':
    player_wins = 'Second'

elif line_one_list[0] == '1' and line_two_list[0] == '1' and line_three_list[0] == '1':
    player_wins = 'First'
elif line_one_list[1] == '1' and line_two_list[1] == '1' and line_three_list[1] == '1':
    player_wins = 'First'
elif line_one_list[2] == '1' and line_two_list[2] == '1' and line_three_list[2] == '1':
    player_wins = 'First'

elif line_one_list[0] == '2' and line_two_list[0] == '2' and line_three_list[0] == '2':
    player_wins = 'Second'
elif line_one_list[1] == '2' and line_two_list[1] == '2' and line_three_list[1] == '2':
    player_wins = 'Second'
elif line_one_list[2] == '2' and line_two_list[2] == '2' and line_three_list[2] == '2':
    player_wins = 'Second'

if player_wins:
    print(f'{player_wins} player won')
else:
    print('Draw!')
