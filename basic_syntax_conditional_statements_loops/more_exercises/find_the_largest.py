number = int(input())
str_of_number = str(number)
list_of_numbers = []
for num in str_of_number:
    list_of_numbers.append(num)
list_of_numbers.sort(reverse=True)
sorted_list = "".join(list_of_numbers)
print(int(sorted_list))
