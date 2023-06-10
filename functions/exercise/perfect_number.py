def perfect(x):
    divisors_list = []
    list_sum = 0
    for i in range(1, x):
        if x % i == 0:
            divisors_list.append(i)
    list_sum = sum(divisors_list)
    if list_sum == x:
        return True


number = int(input())
perfect_number = perfect(number)
if perfect_number:
    print('We have a perfect number!')
else:
    print("It's not so perfect.")
