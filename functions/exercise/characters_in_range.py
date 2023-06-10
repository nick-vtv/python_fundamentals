def chars_in_range(a, b):
    start_char = ord(a) + 1
    end_char = ord(b) - 1
    list_of_chars = []
    for char in range(start_char, end_char + 1):
        list_of_chars.append(chr(char))
    return list_of_chars


char_a = input()
char_b = input()
chars = chars_in_range(char_a, char_b)
print(" ".join(chars))
