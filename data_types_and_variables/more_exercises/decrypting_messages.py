key_value = int(input())
number_of_lines = int(input())
message_list = []
for number in range(number_of_lines):
    letter = input()
    new_letter = chr(ord(letter) + key_value)
    message_list.append(new_letter)
print("".join(message_list))
