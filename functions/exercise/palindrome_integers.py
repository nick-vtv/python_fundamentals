def is_palindrome(x):
    x_str = str(x)
    reversed_x_str = ''
    for string in reversed(x_str):
        reversed_x_str += string
    if x_str == reversed_x_str:
        print(True)
    else:
        print(False)


list_of_integers = list(map(int, input().split(", ")))
for integer in list_of_integers:
    is_palindrome(integer)
