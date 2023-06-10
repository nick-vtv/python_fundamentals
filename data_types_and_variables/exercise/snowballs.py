number_of_snowballs = int(input())

highest_value = 0
weight_of_best = 0
time_of_best = 0
quality_of_best = 0

for snowball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_to_target = int(input())
    quality_of_snowball = int(input())
    current_value = (weight_of_snowball / time_to_target) ** quality_of_snowball
    if current_value > highest_value:
        highest_value = int(current_value)
        weight_of_best = weight_of_snowball
        time_of_best = time_to_target
        quality_of_best = quality_of_snowball

print(f'{weight_of_best} : {time_of_best} = {highest_value} ({quality_of_best})')
