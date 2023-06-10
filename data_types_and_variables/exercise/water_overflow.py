number_of_lines = int(input())
tank_volume = 255
total_water = 0
for i in range(number_of_lines):
    water_liters = int(input())
    if total_water + water_liters <= tank_volume:
        total_water += water_liters
    else:
        print('Insufficient capacity!')
print(total_water)
