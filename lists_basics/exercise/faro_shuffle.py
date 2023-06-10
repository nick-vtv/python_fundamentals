card_list = input().split(" ")
number_of_shuffles = int(input())
for i in range(number_of_shuffles):
    shuffled_list = []
    middle = int(len(card_list) / 2)
    card_list_a = card_list[0:middle:]
    card_list_b = card_list[middle::]
    while card_list_a:
        shuffled_list.append(card_list_a[0])
        shuffled_list.append(card_list_b[0])
        del card_list_a[0]
        del card_list_b[0]
    card_list = shuffled_list

print(card_list)
