number_of_lines = int(input())
opened_bracket = False
BALANCED = False
SPOILED = False
for i in range(number_of_lines):
    symbol = input()
    if symbol == '(' and not opened_bracket:
        opened_bracket = True
        BALANCED = False
    elif symbol == ')' and opened_bracket:
        BALANCED = True
        opened_bracket = False
    elif symbol == '(' and opened_bracket:
        SPOILED = True
    elif symbol == ')' and not opened_bracket:
        SPOILED = True
if BALANCED and not SPOILED:
    print('BALANCED')
else:
    print('UNBALANCED')
