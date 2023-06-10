team_A = []
for a in range(1, 12):
    player_A = 'A-' + str(a)
    team_A.append(player_A)
team_B = []
for b in range(1, 12):
    player_B = 'B-' + str(b)
    team_B.append(player_B)
terminated = False
players_list = input().split(" ")
for player in players_list:
    if player in team_A:
        team_A.remove(player)
    elif player in team_B:
        team_B.remove(player)
    if len(team_A) < 7 or len(team_B) < 7:
        terminated = True
        break
print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')
if terminated:
    print('Game was terminated')
