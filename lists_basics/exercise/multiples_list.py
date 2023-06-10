factor_number = int(input())
count_number = int(input())
multiples_list = []
for i in range(1, count_number + 1):
    multiple = i * factor_number
    multiples_list.append(multiple)
print(multiples_list)
