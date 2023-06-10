def even_number(x):
    if x % 2 == 0:
        return True
    else:
        return False


list_of_integers = list(map(int, input().split()))
list_of_even = list(filter(even_number, list_of_integers))
print(list_of_even)
