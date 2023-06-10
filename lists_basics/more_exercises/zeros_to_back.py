string_as_list = input().split(", ")
modified_integers_list = []
zeroes_list = []
final_list = []
integers_list = []
for string in string_as_list:
    if string == '0':
        zeroes_list.append(string)
    else:
        modified_integers_list.append(string)
final_list = modified_integers_list + zeroes_list
for element in final_list:
    integers_list.append(int(element))
print(integers_list)
