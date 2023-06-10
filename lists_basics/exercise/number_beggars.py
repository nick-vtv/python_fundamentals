string_list = input().split(", ")
number_of_beggars = int(input())
string_of_integers_list = []
beggars_sum_list = []
for string in string_list:
    string_of_integers_list.append(int(string))
for beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for integer in range(beggar, len(string_of_integers_list), number_of_beggars):
        current_beggar_sum += string_of_integers_list[integer]
    beggars_sum_list.append(current_beggar_sum)
print(beggars_sum_list)
