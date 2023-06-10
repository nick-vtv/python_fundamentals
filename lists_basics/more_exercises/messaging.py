sequence_of_numbers_list = input().split()
sequence_of_stings = input()

sequence_of_strings_list = []
sequence_of_integers_list = []
final_list = []
current_index = 0
indexes_list = []

for number in sequence_of_numbers_list:
    sequence_of_integers_list = []
    for digit in number:
        sequence_of_integers_list.append(int(digit))
    current_index = sum(sequence_of_integers_list)
    indexes_list.append(current_index)

for string in sequence_of_stings:
    sequence_of_strings_list.append(string)

for active_index in indexes_list:
    if active_index >= len(sequence_of_strings_list):
        curr_index = active_index - len(sequence_of_strings_list)
        char_to_add = sequence_of_strings_list[curr_index]
        final_list.append(char_to_add)
        del sequence_of_strings_list[curr_index]
    else:
        char_to_add = sequence_of_strings_list[active_index]
        final_list.append(char_to_add)
        del sequence_of_strings_list[active_index]

print("".join(final_list))
