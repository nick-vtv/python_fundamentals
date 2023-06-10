how_many_letters = int(input())
for x in range(97, 97 + how_many_letters):
    for y in range(97, 97 + how_many_letters):
        for z in range(97, 97 + how_many_letters):
            print(chr(x) + chr(y) + chr(z))
