word = input()
list_of_capital_letter_indices = []
for index, letter in enumerate(word):
    if 65 <= ord(letter) <= 90:
        list_of_capital_letter_indices.append(index)
print(list_of_capital_letter_indices)
