text_string = input().lower()
word_list = ['Sand', 'Water', 'Fish', 'Sun']
word_counter = 0
for word in word_list:
    if word.lower() in text_string:
        word_counter += text_string.count(word.lower())
print(word_counter)
