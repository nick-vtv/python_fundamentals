def validate_password(pwd: str):
    length = False
    letters_and_digits = False
    min_2_digits = False

    if len(pwd) in range(6, 11):
        length = True
    else:
        print('Password must be between 6 and 10 characters')

    if pwd.isalnum():
        letters_and_digits = True
    else:
        print('Password must consist only of letters and digits')

    digit_counter = 0
    for symbol in pwd:
        if ord(symbol) in range(48, 58):
            digit_counter += 1
    if digit_counter >= 2:
        min_2_digits = True
    else:
        print('Password must have at least 2 digits')

    if length and letters_and_digits and min_2_digits:
        print('Password is valid')


password = input()
validate_password(password)
