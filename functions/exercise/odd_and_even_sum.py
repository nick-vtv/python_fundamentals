def odd_even_sum(x):
    x_str = str(x)
    even_list = []
    odd_list = []
    for string in x_str:
        if int(string) % 2 == 0:
            even_list.append(int(string))
        else:
            odd_list.append(int(string))
    even_sum = sum(even_list)
    odd_sum = sum(odd_list)
    return odd_sum, even_sum


number = int(input())
sum_of_odd, sum_of_even = odd_even_sum(number)
print(f'Odd sum = {sum_of_odd}, Even sum = {sum_of_even}')
