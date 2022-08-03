import math

num_people = int(input())
capacity = int(input())

elevator_courses = math.ceil(num_people / capacity)
print(elevator_courses)
