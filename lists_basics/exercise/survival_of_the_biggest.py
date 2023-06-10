list_of_numbers = input().split()
count_of_removes = int(input())
list_of_integer_numbers = []
filtered_list = []
for number in list_of_numbers:
    list_of_integer_numbers.append(int(number))
list_of_integer_numbers.sort()
for remove in range(count_of_removes):
    del list_of_integer_numbers[0]
for number in list_of_numbers:
    if int(number) in list_of_integer_numbers:
        filtered_list.append(number)
filtered_list_string = ", ".join(filtered_list)
print(filtered_list_string)
