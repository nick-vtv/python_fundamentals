quantity_of_decors = int(input())
days_to_christmas = int(input())
total = 0
spirit = 0
for day in range(1, days_to_christmas + 1):
    if day % 11 == 0:
        quantity_of_decors += 2
    if day % 2 == 0:
        total += 2 * quantity_of_decors
        spirit += 5
    if day % 3 == 0:
        total += 5 * quantity_of_decors + 3 * quantity_of_decors
        spirit += 3 + 10
    if day % 5 == 0:
        total += 15 * quantity_of_decors
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        total += 5 + 3 + 15
if days_to_christmas % 10 == 0:
    spirit -= 30
print(f'Total cost: {total}')
print(f'Total spirit: {spirit}')
