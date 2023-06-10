animals_string = input()
list_of_animals = animals_string.split(", ")
if list_of_animals[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for index, animal in enumerate(reversed(list_of_animals)):
        if animal == 'wolf':
            print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')
