list_of_gifts = input().split()
command = input()
final_list = []
while command != 'No Money':
    command_list = command.split()
    if command_list[0] == 'OutOfStock':
        if command_list[1] in list_of_gifts:
            for index in range(len(list_of_gifts)-1, -1, -1):
                if list_of_gifts[index] == command_list[1]:
                    list_of_gifts[index] = 'None'
    elif command_list[0] == 'Required':
        if int(command_list[2]) <= (len(list_of_gifts)-1):
            for index in range(len(list_of_gifts)-1, -1, -1):
                if index == int(command_list[2]):
                    list_of_gifts[index] = command_list[1]
    elif command_list[0] == 'JustInCase':
        del list_of_gifts[-1]
        list_of_gifts.append(command_list[1])
    command = input()
for gift in list_of_gifts:
    if gift != 'None':
        final_list.append(gift)
print(" ".join(final_list))
