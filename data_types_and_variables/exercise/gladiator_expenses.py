lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
times_of_broken_shields = 0
total = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        total += helmet_price
    if fight % 3 == 0:
        total += sword_price
        if fight % 2 == 0:
            total += shield_price
            times_of_broken_shields += 1
            if times_of_broken_shields % 2 == 0:
                total += armor_price

print(f'Gladiator expenses: {total:.2f} aureus')
