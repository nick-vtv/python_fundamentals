from math import ceil
people_to_elevate = int(input())
capacity_of_elevator = int(input())
courses = ceil(people_to_elevate / capacity_of_elevator)
print(courses)
