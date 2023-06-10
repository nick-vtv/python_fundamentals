list_of_numbers = input().split(" ")
opposite_numbers_list = []
for number in list_of_numbers:
    opposite_number = -int(number)
    opposite_numbers_list.append(opposite_number)
print(opposite_numbers_list)
