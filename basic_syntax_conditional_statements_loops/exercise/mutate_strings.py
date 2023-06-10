string_one = input()
string_two = input()
last_string = string_one
for x in range(len(string_one)):
    left_string = string_two[:x + 1]
    right_string = string_one[x + 1:]
    new_string = left_string + right_string
    if new_string != last_string:
        print(new_string)
        last_string = new_string
