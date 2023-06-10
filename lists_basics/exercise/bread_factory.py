energy = 100
coins = 100
closed = False
events_list = input().split("|")
for event in events_list:
    current_event_list = event.split("-")
    if current_event_list[0] == 'rest':
        if energy + int(current_event_list[1]) > 100:
            print(f'You gained {100 - energy} energy.')
            energy = 100
        else:
            energy += int(current_event_list[1])
            print(f'You gained {int(current_event_list[1])} energy.')
        print(f'Current energy: {energy}.')
    elif current_event_list[0] == 'order':
        if energy - 30 >= 0:
            energy -= 30
            coins += int(current_event_list[1])
            print(f'You earned {int(current_event_list[1])} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        if coins >= int(current_event_list[1]):
            coins -= int(current_event_list[1])
            print(f'You bought {current_event_list[0]}.')
        else:
            print(f'Closed! Cannot afford {current_event_list[0]}.')
            closed = True
            break
if not closed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
