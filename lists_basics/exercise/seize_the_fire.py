list_of_fire_cells = input().split("#")
amount_of_water = int(input())
total_effort = 0
total_fire = 0
cell_is_valid = False
print('Cells:')
for cell in list_of_fire_cells:
    single_fire_cell = cell.split(" = ")
    if single_fire_cell[0] == 'High' and int(single_fire_cell[1]) in range(81, 126):
        cell_is_valid = True
    elif single_fire_cell[0] == 'Medium' and int(single_fire_cell[1]) in range(51, 81):
        cell_is_valid = True
    elif single_fire_cell[0] == 'Low' and int(single_fire_cell[1]) in range(1, 51):
        cell_is_valid = True
    if cell_is_valid and amount_of_water >= int(single_fire_cell[1]):
        amount_of_water -= int(single_fire_cell[1])
        total_effort += 0.25 * int(single_fire_cell[1])
        total_fire += int(single_fire_cell[1])
        print(f' - {single_fire_cell[1]}')
    if amount_of_water <= 0:
        break
    cell_is_valid = False
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')
